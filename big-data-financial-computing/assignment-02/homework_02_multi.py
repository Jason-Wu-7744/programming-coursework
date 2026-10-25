import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import chi2, f
import akshare as ak

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'


# 读取数据
code_list = ['600021', '000021', '600521', '601021', '600621', '603021', '688021', '603221']
data_list = []

# for i in code_list:
#     data = ak.stock_zh_a_hist(symbol=i,
#                               period="daily",
#                               start_date="20000101",
#                               end_date="20251231")
#     data = data[['日期', '股票代码', '收盘']]
#     data.columns = ['date', 'code', 'close']
#     data['date'] = pd.to_datetime(data['date'])
#     data['return'] = np.log(data['close']) - np.log(data['close'].shift(periods=1))
#     data.dropna(inplace=True)
#     ind = (data['return'] >= -0.1) & (data['return'] <= 0.1)
#     data = data.loc[ind, :]
#     print(data)
#     data_list.append(data)
#
# data_m_r = pd.read_csv("2000-2025上证综指日收益率_日度无风险利率.csv")
# data_m_r['rm-rf'] = data_m_r['return'] - data_m_r['rf']
# data_m_r.columns = ['date', 'rm', 'rf', 'rm-rf']
# data_m_r['date'] = pd.to_datetime(data_m_r['date'])
# print(data_m_r)
#
# # 数据拼接
# data_matrix = pd.merge(left=data_m_r[['date', 'rf', 'rm-rf']],
#                        right=data_list[0][['date', 'return']].rename(columns={'return': 'return_'+code_list[0]}),
#                        on='date',
#                        how='inner',
#                        sort=True)
# data_matrix["ri-rf_"+code_list[0]] = data_matrix['return_'+code_list[0]] - data_matrix['rf']
# for i in range(7):
#     data_matrix = pd.merge(left=data_matrix,
#                            right=data_list[i+1][['date', 'return']].rename(columns={'return': 'return_'+code_list[i+1]}),
#                            on='date',
#                            how='inner',
#                            sort=True)
#     data_matrix["ri-rf_"+code_list[i+1]] = data_matrix['return_'+code_list[i+1]] - data_matrix['rf']
# print(data_matrix)
# data_matrix.to_csv("data_matrix_monthly.csv", index=False)

data_matrix = pd.read_csv("data_matrix_daily.csv")
data_matrix['date'] = pd.to_datetime(data_matrix['date'])
print(data_matrix)
# 由于8只股票中有一支上市时间较晚，时间区间现在收缩到了2020-2025
data_matrix['rm'] = data_matrix['rm-rf'] + data_matrix['rf']


data_matrix_monthly = data_matrix.set_index('date').resample('M').agg({
    'rf': lambda x: (1 + x).prod() - 1,
    'rm': lambda x: x.sum(),
    'return600021': lambda x: x.sum(),
    'return000021': lambda x: x.sum(),
    'return600521': lambda x: x.sum(),
    'return601021': lambda x: x.sum(),
    'return600621': lambda x: x.sum(),
    'return603021': lambda x: x.sum(),
    'return688021': lambda x: x.sum(),
    'return603221': lambda x: x.sum()})
print(data_matrix_monthly)

code_list = ['600021', '000021', '600521', '601021', '600621', '603021', '688021', '603221']


data_matrix_monthly['rreturn_m'] = data_matrix_monthly['rm'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_600021'] = data_matrix_monthly['return600021'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_000021'] = data_matrix_monthly['return000021'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_600521'] = data_matrix_monthly['return600521'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_601021'] = data_matrix_monthly['return601021'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_600621'] = data_matrix_monthly['return600621'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_603021'] = data_matrix_monthly['return603021'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_688021'] = data_matrix_monthly['return688021'] - data_matrix_monthly['rf']
data_matrix_monthly['rreturn_603221'] = data_matrix_monthly['return603221'] - data_matrix_monthly['rf']


# 第一个月份只有最后四天的数据，需要删除
data_matrix_monthly = data_matrix_monthly.iloc[1:, :]
print(data_matrix_monthly)


# 下面开始月度单因子模型的多资产定价
# 先算统计量
# ret_ind 是市场超额收益率
ret_ind = data_matrix_monthly['rreturn_m'].values
# 期数
T = len(ret_ind)
# 股票数
N = len(code_list)
mu_market = np.mean(ret_ind)
# 市场超额收益率的样本方差
sigma_market = np.sum((ret_ind-mu_market)**2)/T
# 股票超额收益率
ret_stocks = data_matrix_monthly[['rreturn_600021', 'rreturn_000021', 'rreturn_600521', 'rreturn_601021', 'rreturn_600621', 'rreturn_603021', 'rreturn_688021', 'rreturn_603221']].values
# 无限制模型
x = np.ones((T, 2))
x[:, 1] = ret_ind
y = ret_stocks
xTx = np.dot(np.transpose(x), x)
xTy = np.dot(np.transpose(x), y)
AB_hat = np.dot(np.linalg.inv(xTx), xTy)
ALPHA = AB_hat[0]
print(ALPHA)
BETA = AB_hat[1]
RESD = y - np.dot(x, AB_hat)
COV = np.dot(np.transpose(RESD), RESD)/T
invCOV = np.linalg.inv(COV)

# 限制模型
xr = np.ones((T, 1))
xr[:, 0] = ret_ind
yr = ret_stocks
xrTxr = np.dot(np.transpose(xr), xr)
xrTyr = np.dot(np.transpose(xr), yr)
ABr_hat = np.dot(np.linalg.inv(xrTxr), xrTyr)
RESDr = yr - np.dot(xr, ABr_hat)
COVr = np.dot(np.transpose(RESDr), RESDr)/T
invCOVr = np.linalg.inv(COVr)

# Wald检验
trans_ALPHA = np.ones((len(ALPHA), 1))
trans_ALPHA[:, 0] = ALPHA
SWchi2 = T*(1/(1+mu_market**2/sigma_market))*np.dot(np.dot(ALPHA, invCOV), trans_ALPHA)
SWF = (T-N-1)/N*(1/(1+mu_market**2/sigma_market))*np.dot(np.dot(ALPHA, invCOV), trans_ALPHA)
pvalue_Wchi2 = 1 - chi2.cdf(SWchi2[0], N)
pvalue_WF = 1 - f.cdf(SWF[0], N, T-N-1)
print("Wald检验-卡方统计量")
print(pvalue_Wchi2)
print("Wald检验-F统计量")
print(pvalue_WF)

# 似然比检验
# print(COVr)
# print(COV)
# print(N)
SLRchi2 = T*(np.log(np.linalg.det(COVr)) - np.log(np.linalg.det(COV)))
pvalue_SLRchi2 = 1 - chi2.cdf(SLRchi2, N)
print("似然比LR检验")
print(pvalue_SLRchi2)

# 拉格朗日乘子检验
a = np.zeros((8, 1))
a[:, 0] =  np.sum(RESDr, axis=0)
salpha = np.dot(invCOVr, a)
b = np.dot(ret_ind, RESDr)
sbeta = np.zeros((8,1))
sbeta[:, 0] = np.dot(invCOVr, b)
score = np.concatenate((salpha, sbeta), axis=0)
print(score)

a = np.concatenate((invCOVr*T, invCOVr*np.sum(ret_ind)), axis=1)
b = np.concatenate((invCOVr*np.sum(ret_ind), invCOVr*np.sum(ret_ind**2)), axis=1)
Minfo = np.concatenate((a, b), axis=0)
SLMchi2 = np.dot(np.dot(np.transpose(score), np.linalg.inv(Minfo)), score)
pvalue_SLMchi2 = 1-chi2.cdf(SLMchi2[0][0], N)
print("拉格朗日乘子LM检验")
print(pvalue_SLMchi2)
#三种算法的p值大致相同，结果应当没有问题，多资产联合起来符合单资产模型

print("-----------------------------------------------------------------------------------------")

# 不妨再做一个日度的单因子多资产的CAPM检验
# 先算统计量
ret_ind = data_matrix['rm-rf'].values
T = len(ret_ind)
N = len(code_list)
mu_market = np.mean(ret_ind)
sigma_market = np.sum((ret_ind-mu_market)**2)/T
ret_stocks = data_matrix[['ri-rf600021', 'ri-rf000021', 'ri-rf600521', 'ri-rf601021', 'ri-rf600621', 'ri-rf603021', 'ri-rf688021', 'ri-rf603221']].values
# 无限制模型
x = np.ones((T, 2))
x[:, 1] = ret_ind
y = ret_stocks
xTx = np.dot(np.transpose(x), x)
xTy = np.dot(np.transpose(x), y)
AB_hat = np.dot(np.linalg.inv(xTx), xTy)
ALPHA = AB_hat[0]
print(ALPHA)
BETA = AB_hat[1]
RESD = y - np.dot(x, AB_hat)
COV = np.dot(np.transpose(RESD), RESD)/T
invCOV = np.linalg.inv(COV)

# 限制模型
xr = np.ones((T, 1))
xr[:, 0] = ret_ind
yr = ret_stocks
xrTxr = np.dot(np.transpose(xr), xr)
xrTyr = np.dot(np.transpose(xr), yr)
ABr_hat = np.dot(np.linalg.inv(xrTxr), xrTyr)
RESDr = yr - np.dot(xr, ABr_hat)
COVr = np.dot(np.transpose(RESDr), RESDr)/T
invCOVr = np.linalg.inv(COVr)

# Wald检验
trans_ALPHA = np.ones((len(ALPHA), 1))
trans_ALPHA[:, 0] = ALPHA
SWchi2 = T*(1/(1+mu_market**2/sigma_market))*np.dot(np.dot(ALPHA, invCOV), trans_ALPHA)
SWF = (T-N-1)/N*(1/(1+mu_market**2/sigma_market))*np.dot(np.dot(ALPHA, invCOV), trans_ALPHA)
pvalue_Wchi2 = 1 - chi2.cdf(SWchi2[0], N)
pvalue_WF = 1 - f.cdf(SWF[0], N, T-N-1)
print(pvalue_Wchi2)
print(pvalue_WF)

# 似然比检验
# print(COVr)
# print(COV)
# print(N)
SLRchi2 = T*(np.log(np.linalg.det(COVr)) - np.log(np.linalg.det(COV)))
pvalue_SLRchi2 = 1 - chi2.cdf(SLRchi2, N)
print(pvalue_SLRchi2)

# 拉格朗日乘子检验
a = np.zeros((8, 1))
a[:, 0] =  np.sum(RESDr, axis=0)
salpha = np.dot(invCOVr, a)
b = np.dot(ret_ind, RESDr)
sbeta = np.zeros((8,1))
sbeta[:, 0] = np.dot(invCOVr, b)
score = np.concatenate((salpha, sbeta), axis=0)
print(score)

a = np.concatenate((invCOVr*T, invCOVr*np.sum(ret_ind)), axis=1)
b = np.concatenate((invCOVr*np.sum(ret_ind), invCOVr*np.sum(ret_ind**2)), axis=1)
Minfo = np.concatenate((a, b), axis=0)
SLMchi2 = np.dot(np.dot(np.transpose(score), np.linalg.inv(Minfo)), score)
pvalue_SLMchi2 = 1-chi2.cdf(SLMchi2[0][0], N)
print(pvalue_SLMchi2)
#三种算法的p值大致相同，结果应当没有问题，多资产联合起来符合单资产模型