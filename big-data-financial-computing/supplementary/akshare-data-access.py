import pandas as pd
import akshare as ak
import numpy as np
import matplotlib.pyplot as plt

# 获取股票历史数据
# symbol: 股票代码（纯数字，无需后缀）
# period: "daily"日线, "weekly"周线, "monthly"月线
# adjust: "qfq"前复权（推荐）, "hfq"后复权, ""不复权
# df = ak.stock_zh_a_hist(
#     symbol="002444",
#     period="daily",
#     start_date="20000101",
#     end_date="20260315")
# print(df)
# print(df.columns)
# # 只保留日期和收盘价两列，并重命名
# df = df[['日期', '收盘']]
# df.columns = ['date', 'close_price']
#
# # 将日期列转换为datetime类型
# df['date'] = pd.to_datetime(df['date'])
#
#
# # 指数
# df_index = ak.index_zh_a_hist(
#     symbol="000001",      # 沪深300指数代码
#     period="daily",       # 日线
#     start_date="20000101",
#     end_date="20251231"
# )
# print(df_index)


# 在选取指数时，沪深300是最为合适的，但是沪深300直到2005年才出现，故使用上证综指
data_index = ak.index_zh_a_hist(symbol="000001",
                                period="monthly",
                                start_date="20000101",
                                end_date="20251231")
data_index = data_index[['日期', '收盘']]
data_index.columns = ['date', 'close']
data_index['date'] = pd.to_datetime(data_index['date'])
data_index['return'] = np.log(data_index['close']) - np.log(data_index['close'].shift(periods=1))
data_index.dropna(inplace=True)
ind = (data_index['return'] >= -0.1) & (data_index['return'] <= 0.1)
data_index = data_index.loc[ind, :]
print(data_index)


# 无风险利率
data_rf = ak.bond_zh_us_rate(start_date="20000101")
data_rf = data_rf[['日期', '中国国债收益率2年']].bfill()
data_rf.columns = ['date', 'CGB2Y']
data_rf['rf'] = data_rf['CGB2Y']/100/12
print(data_rf)

data_m_r = pd.merge(left=data_index,
                    right=data_rf[['date', 'rf']],
                    on='date',
                    how='inner',
                    sort=True)
print(data_m_r)

# plt.figure(1, figsize=(12, 7))
# plt.plot(data_rf['date'], data_rf['CGB2Y'])
# plt.title('中国国债收益率2年2002-2025', fontsize=36)
# plt.xlabel(r'$t$', fontsize=20)
# plt.ylabel(r'$r_f$', fontsize=20)
# plt.savefig('中国国债收益率2年2002-2025.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 使用新浪接口
# data = ak.stock_zh_a_hist(symbol="sz000021",
#                               period="daily",
#                               start_date="20000101",
#                               end_date="20251231")
# data = data[['日期', '股票代码', '收盘']]
# data.columns = ['date', 'code', 'close']
# data['date'] = pd.to_datetime(data['date'])
# data['return'] = np.log(data['close']) - np.log(data['close'].shift(periods=1))
# data.dropna(inplace=True)
# ind = (data['return'] >= -0.1) & (data['return'] <= 0.1)
# data = data.loc[ind, :]
# print(data)