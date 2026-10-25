import numpy as np
import pandas as pd
from math import pi
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn import linear_model
import akshare as ak

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'


# data_600021 = ak.stock_zh_a_hist(
#     symbol="600021",
#     period="daily",
#     start_date="20010101",
#     end_date="20231231",
#     adjust="qfq"
# )
# data_600021.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount',
#               'amplitude', 'pct_change', 'change_amount', 'turnover']
# data_600021.to_csv("data_600021.csv", index=False)

# data_rf = ak.rate_interbank(market="上海银行同业拆借市场", indicator="Shibor人民币", symbol="1M")
# data_rf.columns = ['date', 'rf_rate']
# data_rf.to_csv("data_rf.csv", index=False)

# akshare还是一如既往地难以回复请求。
# 从resset导入日度收盘价、日度成交额、日度无风险利率

# 读取日度数据
data_daily = pd.read_excel("RESSET_DRESSTK_2001_2010_1.xlsx")
data_daily.columns = ['date', 'close', 'aret', 'rf', 'PE', 'EPS', 'ROE']
data_daily_list = ['RESSET_DRESSTK_2011_2015_1.xlsx',
                   'RESSET_DRESSTK_2016_2020_1.xlsx',
                   'RESSET_DRESSTK_2021_2025_1.xlsx',
                   'RESSET_DRESSTK_2021_2025_2.xlsx',
                   'RESSET_DRESSTK_2021_2025_3.xlsx']
for i in data_daily_list:
    data_daily_extra = pd.read_excel(i)
    data_daily_extra.columns = ['date', 'close', 'aret', 'rf', 'PE', 'EPS', 'ROE']
    data_daily = pd.concat([data_daily, data_daily_extra], axis=0).reset_index(drop=True)

data_daily['date'] = pd.to_datetime(data_daily['date'])
# 按时间排序
data_daily = data_daily.sort_values('date').reset_index(drop=True)
# data_daily = data_daily.dropna()
print(data_daily)


# 不妨画一个上海电力收盘价走势图
plt.figure(1, figsize=(16, 9))
plt.plot(data_daily['date'], data_daily['close'], lw=2)
plt.title("上海电力600021股价走势图", fontsize=32)
plt.xlabel("时间")
plt.ylabel("价格（元）")
plt.savefig('上海电力股价走势图.jpg', dpi=300, bbox_inches='tight')
plt.show()


# 读取月度数据
data_monthly = pd.read_excel("RESSET_MRESSTK_1.xlsx")
data_monthly.columns = ['date', 'close', 'tradesum', 'return', 'aret', 'rf', 'PE', 'EPS', 'ROE']
data_monthly['date'] = pd.to_datetime(data_monthly['date'])
data_monthly = data_monthly.dropna()
print(data_monthly)
# 生成年月标识用于匹配
data_daily['year_month'] = data_daily['date'].dt.to_period('M')
data_monthly['year_month'] = data_monthly['date'].dt.to_period('M')



# 开始构造因子和数据
# 月波动率
# 先算日对数收益率
data_daily['return'] = np.log(data_daily['close'])-np.log(data_daily['close'].shift(1))
data_daily = data_daily.dropna()
print(data_daily)
# 计算日度收益率平方，再按月求和 = 月已实现方差（未年化）
daily_r2 = data_daily.groupby('year_month')['return'].apply(lambda x: np.sum(x**2)).reset_index()
daily_r2.columns = ['year_month', 'volatility']
# 合并到月度数据
data_monthly = data_monthly.merge(daily_r2, on='year_month', how='left')
print(data_monthly)

# 月流动性
data_monthly['liquidity'] = np.abs(data_monthly['return']/np.log(data_monthly['tradesum']))
print(data_monthly)

# 月股价高点
# 计算每月日度close最大值
monthly_max_close = data_daily.groupby('year_month')['close'].max().reset_index()
monthly_max_close.columns = ['year_month', 'month_max_close']
# 合并到月度数据（先临时合并计算）
data_monthly['year_month'] = data_monthly['date'].dt.to_period('M')
data_monthly = data_monthly.merge(monthly_max_close, on='year_month', how='left')
# 计算前三个月的月最大值滚动最大
# 需要把年月转成时间索引才能rolling
data_monthly['month_end'] = data_monthly['date'] + pd.offsets.MonthEnd(0)
data_monthly = data_monthly.sort_values('month_end').reset_index(drop=True)
# 设置时间为索引
temp = data_monthly[['month_end', 'month_max_close']].set_index('month_end')
# 前三个月（含当月共3个月）的最大值，shift(1)表示不包含当月
temp['prev_3m_max'] = temp['month_max_close'].rolling(window=3, min_periods=1).max().shift(1)
# 合并回主表
data_monthly['prev_3m_max'] = temp['prev_3m_max'].values
# 计算 closemax = 当月max / 前三个月max
data_monthly['closemax'] = data_monthly['month_max_close'] / data_monthly['prev_3m_max']
# 清理临时列
data_monthly = data_monthly.drop(columns=['month_max_close', 'prev_3m_max', 'month_end'])
print(data_monthly)


# 月已实现偏度
# 文献中的5分高频数据难找，可以使用日度收益率来计算月度偏度
def calc_skew(r):
    """计算月度偏度，r为Series"""
    r = r.dropna()
    if len(r) < 5:
        return np.nan
    r_bar = r.mean()
    sigma = r.std(ddof=0)
    if sigma == 0:
        return np.nan
    return np.mean(((r - r_bar) / sigma) ** 3)
monthly_skew = data_daily.groupby('year_month')['return'].apply(calc_skew).reset_index()
monthly_skew.columns = ['year_month', 'skew']
# 合并到月度数据
data_monthly = data_monthly.merge(monthly_skew, on='year_month', how='left')
print(data_monthly)

# 计算月超额收益率
data_monthly['exreturn'] = data_monthly['return'] = data_monthly['rf']
data_monthly = data_monthly.dropna()
print(data_monthly)

# 整理因子和收益率数据
data = data_monthly[['year_month', 'rf', 'return', 'exreturn', 'volatility', 'liquidity', 'closemax', 'skew']]
print(data)
# data.to_csv("data.csv", index=False)

# 因子向后移动一格
data = pd.concat([data, data[['volatility', 'liquidity', 'closemax', 'skew']].shift(periods=1)], axis=1)
print(data)
data.columns = ['year_month', 'rf', 'return', 'exreturn', 'volatility', 'liquidity', 'closemax', 'skew',
                'volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']
data = data.dropna()
print(data)



# 以上完成了数据的清洗，下面开始检验因子有效性


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



# 单因子检验
# 样本内检验
factor_list = ['volatility', 'liquidity', 'closemax', 'skew']
factorL1_list = ['volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']
# 单因子样本内检验
for i in range(len(factor_list)):
    factor = factor_list[i]
    factorL1 = factorL1_list[i]
    model = smf.ols('exreturn ~ '+str(factorL1), data=data[['exreturn', factorL1]])
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
    datafit = data[['year_month', 'rf', 'return', 'exreturn', factor_list[j], factorL1_list[j]]].copy(deep=True)
    # 深度复制，约等于重新建一个数据框，原数据不会因后续操作改变
    n_in = np.sum(datafit['year_month'] <= '2014-12')
    # 1956前为样本内，后为要预测的样本外
    n_out = np.sum(datafit['year_month'] > '2014-12')
    rout = np.zeros(n_out)
    rmean = np.zeros(n_out)
    rreal = np.zeros(n_out)
    rfree = np.zeros(n_out)
    volt2 = np.zeros(n_out)

    for i in range(n_out):
        # 每预测一项得到一个结果
        # 历史超额收益
        r_fit = datafit['exreturn'].iloc[:(n_in + i)].values
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

        rreal[i] = datafit['exreturn'].iloc[n_in + i]
        rfree[i] = datafit['rf'].iloc[n_in + i]
        rout[i] = r_pred
        rmean[i] = np.mean(datafit['exreturn'].iloc[:(n_in + i)].values)
        volt2[i] = np.sum(datafit['return'].iloc[(n_in + i - 12):(n_in + i)].values ** 2)

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


# 以上为单因子检验
# 下面开始多因子检验

# 多因子模型：OLS线性拟合
factor_out = 'volatility', 'liquidity', 'closemax', 'skew'
datafit = data.copy(deep=True)

n_in = np.sum(datafit['year_month'] <= '2014-12')
n_out = np.sum(datafit['year_month'] > '2014-12')
rout = np.zeros(n_out)
rmean = np.zeros(n_out)
rreal = np.zeros(n_out)
rfree = np.zeros(n_out)
volt2 = np.zeros(n_out)

for i in range(n_out):
    r_fit = datafit['exreturn'].iloc[:n_in + i].values
    X_fit = datafit[['volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']].iloc[:(n_in + i), :].values
    X_pred = datafit[['volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']].iloc[(n_in + i), :].values.reshape(1, -1)
    linfits = linear_model.LinearRegression()
    linfits.fit(X_fit, r_fit)
    r_pred = linfits.predict(X_pred)

    rreal[i] = datafit['exreturn'].iloc[n_in + i]
    rfree[i] = datafit['exreturn'].iloc[n_in + i]
    rout[i] = r_pred
    rmean[i] = np.mean(datafit['exreturn'].iloc[:(n_in + i)].values)
    volt2[i] = np.sum(datafit['return'].iloc[(n_in + i - 12):(n_in + i)].values ** 2)

print()
print('Out-of-sample tests for multi-factor model with OLS:')
# print(type(factor_out), factor_out)
print('Predictors: {:s}'.format(', '.join(factor_out)))
R2os, MFSEadj, pvalue_MFSEadj = myfun_stat_gains(rout, rmean, rreal)
Uout, Umean, DeltaU = myfun_econ_gains(rout, rmean, rreal, rfree, volt2, gmm=5)
del datafit


# 可以把fit变成机器学习的
# 样本外检验
# 多因子模型：LASSO回归, Ridge回归，ElasticNet回归
factor_out = 'volatility', 'liquidity', 'closemax', 'skew'
factor_list = np.array(['volatility', 'liquidity', 'closemax', 'skew'])

datafit = data.copy(deep=True)

n_in = np.sum(datafit['year_month'] <= '2014-12')
n_out = np.sum(datafit['year_month'] > '2014-12')
rout = np.zeros(n_out)
rmean = np.zeros(n_out)
rreal = np.zeros(n_out)
rfree = np.zeros(n_out)
volt2 = np.zeros(n_out)

# 自动寻找最优正则化强度
# reg = sklm.LassoCV(random_state=0, cv=10, fit_intercept=True, normalize=True, precompute='auto', copy_X=True, n_jobs=-1, max_iter=10**9, tol=10-6)
# reg_lasso = linear_model.LassoLarsCV(cv=10, fit_intercept=True, normalize=True, precompute='auto', copy_X=True, n_jobs=-1, max_iter=10000000)
# reg = sklm.RidgeCV(cv=10, fit_intercept=True)
# reg = sklm.ElasticNetCV(random_state=0, cv=10, fit_intercept=True, normalize=True, precompute='auto', copy_X=True, n_jobs=-1, max_iter=10**9, tol=10-6)
for i in range(n_out):
    r_fit = datafit['exreturn'].iloc[:(n_in+i)].values
    X_fit = datafit[['volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']].iloc[:(n_in+i), :].values
    X_pred = datafit[['volatilityL1', 'liquidityL1', 'closemaxL1', 'skewL1']].iloc[(n_in+i), :].values.reshape(1, -1)
    # 三种机器学习：LASSO、Ridge和ElasticNet可以切换
    # fits = linear_model.Lasso(alpha=0.001, max_iter=10**6, tol=10-6)
    # fits = linear_model.Ridge(alpha=0.001, max_iter=10**6, tol=10-6)
    fits = linear_model.ElasticNet(alpha=0.001, l1_ratio = 0.6, max_iter=10**6, tol=10-6)
    fits.fit(X_fit, r_fit)
    r_pred = fits.predict(X_pred)
    # print(r_pred)

    rreal[i] = datafit['exreturn'].iloc[n_in+i]
    rfree[i] = datafit['rf'].iloc[n_in+i]
    rout[i] = r_pred[0]
    rmean[i] = np.mean(datafit['exreturn'].iloc[:(n_in+i)].values)
    volt2[i] = np.sum(datafit['return'].iloc[(n_in+i-12):(n_in+i)].values**2)

print('Out-of-sample tests for multi-factor model with ML method:')
print('Predictors: {:s}'.format(', '.join(factor_out)))
R2os, MFSEadj, pvalue_MFSEadj = myfun_stat_gains(rout, rmean, rreal)
Uout, Umean, DeltaU = myfun_econ_gains(rout, rmean, rreal, rfree, volt2, gmm=5)
del datafit

