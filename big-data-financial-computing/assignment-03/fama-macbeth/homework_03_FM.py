import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from scipy.stats import t
plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'

# # 读取市值、盈利价格比数据
# data = pd.read_csv('RESSET_MRESSTK_1.csv', encoding='GB2312', usecols=range(8))
# # 用循环读数据
# for i in range(2, 9):
#     data_read = pd.read_csv('RESSET_MRESSTK_' + str(i) + '.csv', encoding='GB2312', usecols=range(8))
#     data = pd.concat((data, data_read), axis=0, ignore_index=True)
#     del data_read
# # 区分市值与流通市值
# data.columns = ['stk', 'date', 'close', 'fshare', 'tshare', 'monret', 'monrf', 'pe']
# # 流通股本/流通股数（Float Shares）总股本（Total Shares） 月度收益率（Monthly Return） 月度无风险利率（Monthly Risk-free Rate）
# print(data)
#
# data['date'] = pd.to_datetime(data['date'])
# data['yearmonth'] = data['date'].dt.strftime('%Y%m').astype(int)
# # 计算流通市值
# data['stksize'] = data['close']*data['fshare']
# # 计算盈利价格比
# data['stkep'] = 1/data['pe']
# # 月度超额收益率（Monthly Excess Return）
# data['monexcret'] = data['monret'] - data['monrf']
# data.dropna(inplace=True)
# print(data)
#
# # 读取capm的β数据，这里选取36个月回归得出的β
# # encoding只有read_csv才有用，read_excel不需要
# data_beta = pd.read_excel("RESSET_SMONRETBETA_BFDT36_1.xlsx")
# print(data_beta)
# for i in range(2, 7):
#     data_read = pd.read_excel('RESSET_SMONRETBETA_BFDT36_' + str(i) + '.xlsx')
#     data_beta = pd.concat((data_beta, data_read), axis=0, ignore_index=True)
#     # 优化内存
#     del data_read
# data_beta.columns = ['stk', 'date', 'beta']
# data_beta['date'] = pd.to_datetime(data_beta['date'])
# print(data_beta)
#
# data = pd.merge(left=data,
#                 right=data_beta,
#                 on=['stk', 'date'],
#                 how='inner')
# print(data)
# print(data.columns)
# data.to_csv('data.csv', index=False)


data = pd.read_csv('data.csv')
data['date'] = pd.to_datetime(data['date'])
print(data)

# 现在做的是横截面检验，绝不能把所有数据代入一个回归
# 每个月度截面内，用所有股票的当期数据做回归：
# 先看有多少月份
uym = np.unique(data['yearmonth'].values)
print(len(uym))
print(uym)
stk_num = []
# 定义存储系数的列表
const_list = []
size_list = []
ep_list = []
beta_list = []
for i in range(len(uym)):
    data_reg = data[data['yearmonth'] == uym[i]]
    # print(data_reg)
    stk_num.append(len(data_reg['stk']))
    # 开始对每一个时点回归
    print("对"+str(uym[i])+"进行横截面检验")
    x = data_reg.loc[:, ['stksize', 'stkep', 'beta']].values
    X = sm.add_constant(x)
    Y = data_reg.loc[:, ['monexcret']]
    model = sm.OLS(Y, X)
    results = model.fit()
    # print(results.summary())
    const_list.append(results.params[0])
    size_list.append(results.params[1])
    ep_list.append(results.params[2])
    beta_list.append(results.params[3])
plt.figure(1, figsize=(16, 7))
x_num = np.linspace(2004, 2024, 240)
plt.plot(x_num, stk_num, lw=2)
plt.xticks([2004, 2009, 2014, 2019, 2024])
plt.title("2004-2023中国股市上市公司数量", fontsize=36)
plt.xlabel("年份")
plt.ylabel("数量")
plt.savefig('2004-2023中国股市上市公司数量.jpg', dpi=300, bbox_inches='tight')
print(const_list)
print(size_list)
print(ep_list)
print(beta_list)

# 开始计算Fama-MacBeth统计量
def fm_report(coef_list, name, T=None):
    """计算Fama-MacBeth统计量"""
    arr = np.array(coef_list)
    T = len(arr) if T is None else T

    mean = np.mean(arr)  # FM估计量
    std = np.std(arr, ddof=1)  # 时间序列标准差
    se = std / np.sqrt(T)  # 标准误（根号T法则）
    t_stat = mean / se  # t统计量
    # 关心是否有显著性，所以看双尾p值
    p_value = 2*(1 - t.cdf(abs(t_stat), T-1))

    print(f"{name:8s}{mean:+.4f}    {se:.4f}    {t_stat:+.2f}    {p_value:.2f}")
    return mean, t_stat, p_value


# ===== 输出结果 =====
print(f"Fama-MacBeth回归结果 (T={len(const_list)}个月)")
print("-" * 50)
print(f"{'变量':<8}{'系数均值':>4}{'标准误':>8}{'t值':>8}{'p值':>6}")
print("-" * 50)

fm_report(const_list, "Cons")
fm_report(size_list, "Size")  # 期望负号（小市值高收益）
fm_report(ep_list, "EP")  # 期望正号（高EP高收益）
fm_report(beta_list, "Beta")