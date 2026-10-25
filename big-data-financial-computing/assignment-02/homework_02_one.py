import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import akshare as ak

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'

code_list = ['600021', '000021', '600521', '601021', '600621', '603021', '688021', '603221']
data_list = []

for i in code_list:
    data = ak.stock_zh_a_hist(symbol=i,
                              period="daily",
                              start_date="20000101",
                              end_date="20251231")
    data = data[['日期', '股票代码', '收盘']]
    data.columns = ['date', 'code', 'close']
    data['date'] = pd.to_datetime(data['date'])
    data['return'] = np.log(data['close']) - np.log(data['close'].shift(periods=1))
    data.dropna(inplace=True)
    ind = (data['return'] >= -0.1) & (data['return'] <= 0.1)
    data = data.loc[ind, :]
    print(data)
    data_list.append(data)

# data = pd.concat([data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7]], axis=0)
# print(data)
# 试图把八只股票全部代入一个回归中是-绝对错误的，现在进行的是单因子单资产的检验，联合检验需要用到极大似然估计/OLS估计加上三种检验方法。

# # 在选取指数时，沪深300是最为合适的，但是沪深300直到2005年才出现，故使用上证综指
# data_index = ak.index_zh_a_hist(symbol="000001",
#                                 period="daily",
#                                 start_date="20000101",
#                                 end_date="20251231")
# data_index = data_index[['日期', '收盘']]
# data_index.columns = ['date', 'close']
# data_index['date'] = pd.to_datetime(data_index['date'])
# data_index['return'] = np.log(data_index['close']) - np.log(data_index['close'].shift(periods=1))
# data_index.dropna(inplace=True)
# ind = (data_index['return'] >= -0.1) & (data_index['return'] <= 0.1)
# data_index = data_index.loc[ind, :]
# print(data_index)
# plt.figure(1, figsize=(12, 7))
# plt.plot(data_index['date'], data_index['close'])
# plt.title('上证综指2000-2025', fontsize=36)
# plt.xlabel(r'$t$', fontsize=20)
# plt.ylabel(r'$r_m$', fontsize=20)
# plt.savefig('上证综指2000-2025', dpi=300, bbox_inches='tight')
# # plt.show()
#
#
# # 无风险利率
# data_rf = ak.bond_zh_us_rate(start_date="20000101")
# 只有2002及以后的数据，故2000、2001年的数据用2002年第一天的补足
# data_rf = data_rf[['日期', '中国国债收益率2年']].bfill()
# data_rf.columns = ['date', 'CGB2Y']
# data_rf['date'] = pd.to_datetime(data_rf['date'])
# data_rf['rf'] = data_rf['CGB2Y']/100/365
# print(data_rf)
# plt.figure(2, figsize=(12, 7))
# plt.plot(data_rf['date'], data_rf['CGB2Y'])
# plt.title('中国2年期国债收益率2002-2025', fontsize=36)
# plt.xlabel(r'$t$', fontsize=20)
# plt.ylabel(r'$r_f$', fontsize=20)
# plt.savefig('中国2年期国债收益率2002-2025.jpg', dpi=300, bbox_inches='tight')
# # plt.show()
#
# data_m_f = pd.merge(left=data_index[['date', 'return']],
#                     right=data_rf[['date', 'rf']],
#                     on='date',
#                     how='inner')
# print(data_m_f)
#
# data_m_f.to_csv('2000-2025上证综指日收益率_日度无风险利率.csv', index=False)

data_m_r = pd.read_csv("2000-2025上证综指日收益率_日度无风险利率.csv")
data_m_r['rm-rf'] = data_m_r['return'] - data_m_r['rf']
data_m_r.columns = ['date', 'rm', 'rf', 'rm-rf']
data_m_r['date'] = pd.to_datetime(data_m_r['date'])
print(data_m_r)

# 以上完成了数据的收集
# 下面开始对每一个资产回归
for i in range(8):
    print("对"+code_list[i]+"进行单因子单资产的CAPM检验")
    merge_data = pd.merge(left=data_list[i][['date', 'return']],
                          right=data_m_r[['date', 'rm-rf', 'rf']],
                          on='date',
                          how='inner')
    merge_data['ri-rf'] = merge_data['return']-merge_data['rf']
    # print(merge_data)
    ri_rf = merge_data['ri-rf'].values
    rm_rf = merge_data['rm-rf'].values
    plt.figure(i, figsize=(12, 7))
    plt.plot(ri_rf, rm_rf, 'o', ms=5, mfc='w', lw=2)
    plt.title(code_list[i]+"超额收益率与指数超额收益率散点图", fontsize=36)
    plt.xlabel(r'$r_m - r_f$', fontsize=20)
    plt.ylabel(r'$r_i - r_f$', fontsize=20)
    plt.savefig(code_list[i]+"超额收益率与指数超额收益率散点图.jpg", dpi=300, bbox_inches='tight')
    plt.show()
    X = sm.add_constant(rm_rf)
    y = ri_rf
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())