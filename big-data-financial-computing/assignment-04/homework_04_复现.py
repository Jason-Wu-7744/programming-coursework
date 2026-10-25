import numpy as np
import pandas as pd
from math import pi
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn import linear_model

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'

# 在sample4中已经实现了多因子的样本外的OLS和LASSO、Ridge和ElasticNet三种机器学习回归
# 这里进行用12个因子的单因子检验
# 单因子检验分为样本内和样本外检验
# 样本内检验使用回归系数的beta的t检验即可
# 样本外检验分为统计显著性检验和经济显著性检验，通过函数定义可以实现。当然，前提是需要使用回归出的β来推测下一个超额收益率。
# 统计显著性检验有R2OS和di两种方法，经济显著性检验使用U即可

# 导入整理过后的1927以后的数据
data = pd.read_csv("data.csv")
print(data)

# 统计显著性检验函数
def myfun_stat_gains(rout, rmean, rreal):
    # 预测变量，均值变量，实际收益率
    R2os = 1 - np.sum((rreal-rout)**2)/np.sum((rreal-rmean)**2)
    d = (rreal - rmean)**2 - ((rreal-rout)**2 - (rmean-rout)**2)
    x = sm.add_constant(np.arange(len(d))+1)
    model = sm.OLS(d, x)
    fitres = model.fit()
    MFSEadj = fitres.tvalues[0]
    # 返回截距项的t值
    pvalue_MFSEadj = fitres.pvalues[0]

    if (R2os > 0) & (pvalue_MFSEadj <= 0.01):
        jud = '在1%的显著性水平下有样本外预测能力'
    elif (R2os > 0) & (pvalue_MFSEadj > 0.01) & (pvalue_MFSEadj <= 0.05):
        jud = '在5%的显著性水平下有样本外预测能力'
    elif (R2os > 0) & (pvalue_MFSEadj > 0.05) & (pvalue_MFSEadj <= 0.1):
        jud = '在10%的显著性水平下有样本外预测能力'
    else:
        jud = '无样本外预测能力'
    print('Stat gains: R2os = {:f}, MFSEadj = {:f}, MFSEpvalue = {:f}'.format(R2os, MFSEadj, pvalue_MFSEadj))
    print('Inference: {:s}'.format(jud))

    return R2os, MFSEadj, pvalue_MFSEadj


# 经济显著性检验函数
def myfun_econ_gains(rout, rmean, rreal, rfree, volt2, gmm = 5):
    # 预测收益率，均值收益率，实际收益率，无风险利率，收益率方差，风险厌恶系数
    # 风险资产比例
    omg_out = rout/volt2/gmm
    # 下一时刻的组合收益率
    rp_out = rfree + omg_out*rreal
    # 计算效用
    Uout = np.mean(rp_out) - 0.5*gmm*np.var(rp_out)
    # 利用历史均值模型再算一个效用
    omg_mean = rmean/volt2/gmm
    rp_mean = rfree + omg_mean*rreal
    Umean = np.mean(rp_mean) - 0.5*gmm*np.var(rp_mean)
    # 投资人为获得超过历史平均预测而愿意支付的年化管理费用
    DeltaU = Uout - Umean

    if DeltaU < 10**-6:
        jud = '没有经济意义'
    else:
        jud = '有经济意义'
    print('Econ Gains: Delta U = {:f}, Upred = {:f}, Umean = {:f}'.format(DeltaU, Uout, Umean))
    print('Inference: {:s}'.format(jud))

    return Uout, Umean, DeltaU



factor_list = ['DP', 'EP', 'VOL', 'BILL', 'BOND', 'TERM', 'CREDIT', 'PPIG', 'IPG', 'MA112', 'MA312', 'MOM6']
factorL1_list = ['DPL1', 'EPL1', 'VOLL1', 'BILLL1', 'BONDL1', 'TERML1', 'CREDITL1', 'PPIGL1', 'IPGL1', 'MA112L1', 'MA312L1', 'MOM6L1']
# 单因子样本内检验
for i in range(len(factor_list)):
    factor = factor_list[i]
    factorL1 = factorL1_list[i]
    model = smf.ols('ExRet ~ '+str(factorL1), data=data[['ExRet', factorL1]])
    results = model.fit()
    rg_con = results.params['Intercept']
    rg_con_pvalue = results.pvalues['Intercept']
    rg_DP = results.params[factorL1]
    rg_DP_pvalue = results.pvalues[factorL1]
    if rg_DP_pvalue <= 0.01:
        jud = '在1%的显著性水平下有样本内预测能力'
    elif (rg_DP_pvalue > 0.01) & (rg_DP_pvalue <= 0.05):
        jud = '在5%的显著性水平下有样本内预测能力'
    elif (rg_DP_pvalue > 0.05) & (rg_DP_pvalue <= 0.1):
        jud = '在10%的显著性水平下有样本内预测能力'
    else:
        jud = '无样本内预测能力'
    print('In-sample tests for one factor model with OLS:')
    print('Predictor: {:s}'.format(factor))
    print('Regressing Results:  b = {:f},  k = {:f}'.format(rg_con, rg_DP))
    print('Regressing Pvalues: pb = {:f}, pk = {:f}'.format(rg_con_pvalue, rg_DP_pvalue))
    print('Inference: {:s}'.format(jud))
    print("\n")


# 单因子样本外检验
for j in range(len(factor_list)):
    factor_out = factor_list[j]
    num_factor = j
    datafit = data[['yyyymm', 'Ret', 'Rfree', 'ExRet', factor_list[j], factorL1_list[j]]].copy(deep=True)
    # 深度复制，约等于重新建一个数据框，原数据不会因后续操作改变
    n_in = np.sum(datafit['yyyymm'] <= 195612)
    # 1956前为样本内，后为要预测的样本外
    n_out = np.sum(datafit['yyyymm'] > 195612)
    rout = np.zeros(n_out)
    rmean = np.zeros(n_out)
    rreal = np.zeros(n_out)
    rfree = np.zeros(n_out)
    volt2 = np.zeros(n_out)

    for i in range(n_out):
        # 每预测一项得到一个结果
        # 历史超额收益
        r_fit = datafit['ExRet'].iloc[:(n_in + i)].values
        # 历史因子
        X_fit = datafit[factorL1_list[j]].iloc[:(n_in + i)].values
        # 下一期因子值，已知的，用于预测下一期收益
        X_pred = datafit[factorL1_list[j]].iloc[n_in + i]
        # 线性模型
        if num_factor == j:
            X_fit = X_fit.reshape(-1, 1)
            X_pred = X_pred.reshape(-1, 1)
        linfits = linear_model.LinearRegression()
        linfits.fit(X_fit, r_fit)
        r_pred = linfits.predict(X_pred)

        # 不同方式的回归
        #     # model = smf.ols('ExRet ~ DPL1', data=datafit[['ExRet', 'DPL1']].iloc[:(n_in+i),:])
        #     # results = model.fit()
        #     # b = results.params['Intercept']
        #     # k = results.params['DPL1']
        #     # f = datafit['DP'].iloc[n_in+i-1]
        #     # r_pred = k*f+b

        rreal[i] = datafit['ExRet'].iloc[n_in + i]
        rfree[i] = datafit['Rfree'].iloc[n_in + i]
        rout[i] = r_pred
        rmean[i] = np.mean(datafit['ExRet'].iloc[:(n_in + i)].values)
        volt2[i] = np.sum(datafit['Ret'].iloc[(n_in + i - 12):(n_in + i)].values ** 2)

    # 保存预测数据
    df = pd.DataFrame({'return': rreal,
                       'risk free return': rfree,
                       'predicting return': rout,
                       'historical mean return': rmean,
                       'volatility': volt2})
    df.to_csv('data_return.csv', index=False)
    # 检验是否可行
    print()
    print('Out-of-sample tests for one factor model with OLS:')
    print('Predictor: {:s}'.format(factor_out))
    R2os, MFSEadj, pvalue_MFSEadj = myfun_stat_gains(rout, rmean, rreal)
    Uout, Umean, DeltaU = myfun_econ_gains(rout, rmean, rreal, rfree, volt2, gmm=5)
    del datafit