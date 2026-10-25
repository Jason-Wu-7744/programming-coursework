import numpy as np
import pandas as pd
import requests
from scipy.stats import norm, chi2, genpareto, t as t_dist
import matplotlib.pyplot as plt
from arch import arch_model

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'


data = pd.read_excel("上海电力_600021_上市以来日度收盘价---7b9a77f4-7e7c-4908-9e09-571f1e2606c2.xlsx")
data.columns = ['date', 'close']
data['date'] = pd.to_datetime(data['date'])
print(data)

data['return'] = np.log(data['close']) - np.log(data['close']).shift(1)
# 剔除分红等导致的异常收益率
data = data[(data['return'] >= -0.1) & (data['return'] <= 0.1) & (data['return'] != 0)].reset_index(drop=True)
print(data)

plt.figure(1, figsize=(16, 12))
plt.subplot(2, 1, 1)
plt.plot(data['date'], data['close'], lw=2)
plt.title("上海电力股价走势图", fontsize=24)
plt.ylabel("股价")
plt.subplot(2, 1, 2)
plt.plot(data['date'], data['return'])
plt.title("上海电力收益率", fontsize=24)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.savefig('上海电力走势.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 布尔索引
ind = data['date'] >= pd.to_datetime('2003-10-29', format='%Y-%m-%d')
# 先用上面的 ind 筛选出该日期及之后的所有行，再提取其中的 return 列，转成 numpy 数组
r = data[ind]['return'].values*100



# RiskMetrics方法
# 假设满足正态分布，算正态分布参数
l = np.fix(len(r)/3).astype(int)
VaR_RM = np.zeros(len(r))
qalpha = norm.ppf(0.05)
# qalpha是ppt中的zα
# ppf 是 "Percent Point Function"（分位点函数），也就是 CDF（累积分布函数）的反函数。
# 用历史数据算μ和σ
# 三分之一长度后开始估计
for i in range(l, len(r)):
    # 每次估计用前50天的样本
    mhat, shat = norm.fit(r[i-50:i])
    VaR_RM[i] = -(mhat + qalpha*shat)
plt.figure(2, figsize=(16, 9))
plt.plot(data[ind]['date'], r)
# VaR算出来是正值
plt.plot(data[ind]['date'], VaR_RM*-1, lw=2)
plt.title("上海电力VaR（RiskMetrics方法：假设收益率满足正态分布）", fontsize=24)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.legend(['收益率', 'VaR_RM'])
plt.savefig('上海电力VaR（RiskMetrics方法：假设收益率满足正态分布）.jpg', dpi=300, bbox_inches='tight')
# plt.show()



# RiskMetrics方法
# 改用收益率的经验分布
# 似乎就是历史模拟法




# GARCH-Normal方法
VaR_GN = np.zeros(len(r))
for i in range(l, len(r)):
    am_ar_garch = arch_model(r[i - 200:i], mean='ar', lags=1, vol='garch', p=2, q=2, dist='normal')
    # am_ar_garch = arch_model(r[i - 200:i], mean='ar', lags=1, vol='garch', p=1, q=1, dist='normal')
    # disp='off' — 关闭迭代输出
    res_ar_garch = am_ar_garch.fit(disp='off')
    # 向前预测1天，align='origin' — 预测结果按起始点对齐
    a = res_ar_garch.forecast(horizon=1, align='origin')
    mu = a.mean['h.1'].iloc[-1]
    sgm2 = a.variance['h.1'].iloc[-1]
    VaR_GN[i] = -(mu + qalpha * np.sqrt(sgm2))
plt.figure(3, figsize=(16, 9))
plt.plot(data[ind]['date'], r)
plt.plot(data[ind]['date'], VaR_GN * -1)
plt.title("上海电力VaR（GARCH-Normal方法）", fontsize=24)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.legend(['收益率', 'VaR_GN'])
plt.savefig('上海电力VaR（GARCH-Normal方法）.jpg', dpi=300, bbox_inches='tight')
# plt.show()
# 注意到在收益率连续为0的时候，GARCH会不收敛，所以需要去除收益率为0的情况
# GARCH（2，2）的效果似乎并不好



# # GARCH-t方法
# VaR_Gt = np.zeros(len(r))
# for i in range(l, len(r)):
#     am_ar_garch = arch_model(r[i - 200:i], mean='ar', lags=1, vol='garch', p=2, q=2, dist='t')
#     # disp='off' — 关闭迭代输出
#     res_ar_garch = am_ar_garch.fit(disp='off')
#     # 向前预测1天，align='origin' — 预测结果按起始点对齐
#     a = res_ar_garch.forecast(horizon=1, align='origin')
#     mu = a.mean['h.1'].iloc[-1]
#     sgm2 = a.variance['h.1'].iloc[-1]
#     # 从拟合结果中提取自由度 nu
#     # t 分布（Student's t）的标准形式是 t(ν) ，它有一个自由度参数nu
#     nu = res_ar_garch.params['nu']
#     qalpha_t = t_dist.ppf(0.05, nu)
#     VaR_Gt[i] = -(mu + qalpha_t * np.sqrt(sgm2))
# plt.figure(31, figsize=(16, 9))
# plt.plot(data[ind]['date'], r)
# plt.plot(data[ind]['date'], VaR_Gt * -1)
# plt.title("上海电力VaR（GARCH-t方法）", fontsize=24)
# plt.xlabel("时间")
# plt.ylabel("收益率")
# plt.legend(['收益率', 'VaR_Gt'])
# plt.savefig('上海电力VaR（GARCH-t方法）.jpg', dpi=300, bbox_inches='tight')
# # plt.show()
# # 注意到在收益率连续为0的时候，GARCH会不收敛，所以需要去除收益率为0的情况
# # GARCH（2，2）的效果似乎并不好




# 历史模拟法
VaR_HS = np.zeros(len(r))
qalpha = int(200*0.05)
for i in range(l, len(r)):
    his_sample = r[i-200:i]
    his_sample = np.sort(his_sample)
    VaR_HS[i] = -his_sample[qalpha-1]
plt.figure(4, figsize=(16, 9))
plt.plot(data[ind]['date'], r)
plt.plot(data[ind]['date'], VaR_HS*-1, lw=2)
plt.title("上海电力VaR（历史模拟方法）", fontsize=24)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.legend(['收益率', 'VaR_HS'])
plt.savefig('上海电力VaR（历史模拟方法）.jpg', dpi=300, bbox_inches='tight')
# plt.show()



# POT方法
VaR_EVT = np.zeros(len(r))
alpha = 0.05
for i in range(l, len(r)):
    # 历史200个数据点
    his_sample = r[i - 200:i]
    # 排序
    his_sample = np.sort(his_sample)
    # 最小十分之一为极端值
    # 取样本长度的 10% 并向下取整，得到极值样本的个数。
    # np.fix(...)向零取整（截断小数）.astype(int)强制转换数据类型为整数
    # ind最终得到的整数索引，表示"前 10% (不能小于5%)的样本个数"
    ind = np.fix(len(his_sample) * 0.1).astype(int)
    # 取排序后前 10% 的样本作为极值样本，对其取绝对值。
    evt_sample = np.abs(his_sample[:ind])
    # 取第 10% 位置的那个值作为阈值 u 。
    u = np.abs(his_sample[ind])
    exceed_values = evt_sample - u
    n = len(his_sample)
    Nu = len(exceed_values)
    # 最终得到的样本和广义帕累托分布GPD做拟合
    parmhat = genpareto.fit(exceed_values, floc=0)
    print(parmhat)
    # 得到参数
    kHat = parmhat[0]
    sigmaHat = parmhat[2]  # scale parameter
    # 和PPT公式不同，这里用alpna，因为算出来的VaR是正的
    VaR_EVT[i] = u + sigmaHat / kHat * ((alpha * n / Nu) ** -kHat - 1)
ind = data['date'] >= pd.to_datetime('2003-10-29', format='%Y-%m-%d')
plt.figure(5, figsize=(16, 9))
plt.plot(data[ind]['date'], r)
plt.plot(data[ind]['date'], VaR_EVT * -1, lw=2)
plt.title("上海电力VaR（POT方法）", fontsize=24)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.legend(['收益率', 'VaR_EVT'])
plt.savefig('上海电力VaR（POT方法）.jpg', dpi=300, bbox_inches='tight')
plt.show()

data = pd.DataFrame({'return': r,
                     'VaR_RM': VaR_RM,
                     'VaR_GN': VaR_GN,
                     'VaR_HS': VaR_HS,
                     'VaR_EVT': VaR_EVT})
data.to_csv('Data_VaR.csv')


# 尝试GARCH(1, 1)
# data = pd.DataFrame({'return': r,
#                      'VaR_RM': VaR_RM,
#                      'VaR_GN': VaR_GN,
#                      'VaR_HS': VaR_HS,
#                      'VaR_EVT': VaR_EVT})
# data.to_csv('Data_VaR_GARCH(1, 1).csv')

# # 尝试GARCH-t
# data = pd.DataFrame({'return': r,
#                      'VaR_RM': VaR_RM,
#                      'VaR_Gt': VaR_Gt,
#                      'VaR_HS': VaR_HS,
#                      'VaR_EVT': VaR_EVT})
# data.to_csv('Data_VaR_GARCH-t.csv')