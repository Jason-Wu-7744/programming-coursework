import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'

# 读取股票数据
data_stock = pd.read_excel("股票.xlsx")[['日期', 'TCL科技', '美的集团', '五粮液', '中国移动', '立讯精密', '牧原股份', '宁德时代', '迈瑞医疗', '招商银行', '三一重工']]
print(data_stock)
# data_stock = data_stock[['日期', 'TCL科技', '美的集团', '五粮液', '中国移动', '立讯精密', '牧原股份', '宁德时代', '迈瑞医疗', '招商银行', '三一重工']]
data_stock.columns = ['date', '000100', '000333', '000858', '600941', '002475', '002714', '300750', '300760', '600036', '600031']
data_stock['date'] = pd.to_datetime(data_stock['date'])
print(data_stock)

# 读取期货数据
data_futures = pd.read_excel("期货.xlsx")
data_futures.columns = ['date', 'IF', 'IH', 'IC', 'IM']
data_futures['date'] = pd.to_datetime(data_futures['date'])
print(data_futures)

# 计算股票对数收益率
return_stock = np.log(data_stock.iloc[:, 1:]/data_stock.iloc[:, 1:].shift(1))
return_stock = return_stock.dropna()
print(return_stock)

# 计算期货对数收益率
return_futures = np.log(data_futures.iloc[:, 1:]/data_futures.iloc[:, 1:].shift(1))
return_futures = return_futures.dropna()
print(return_futures)

# 构造投资组合
return_stock['portfolio'] = return_stock.mean(axis=1)
print(return_stock)

# 展示股票选择与投资组合收益率
plt.figure(1, figsize=(16, 9))
plt.plot(data_stock['date'][1:], return_stock['portfolio'], lw=2)
plt.title("投资组合收益率", fontsize=32)
plt.xlabel("时间")
plt.ylabel("收益率")
plt.plot(data_stock['date'][1:], return_futures['IF'], lw=2)
plt.plot(data_stock['date'][1:], return_futures['IH'], lw=2)
plt.plot(data_stock['date'][1:], return_futures['IC'], lw=2)
plt.plot(data_stock['date'][1:], return_futures['IM'], lw=2)
plt.legend(['投资组合', 'IF沪深300期货', 'IH上证50期货', 'IC中证500期货', 'IM中证1000期货'])
plt.savefig('投资组合收益率.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 投资组合累积收益率
# （对数收益率的累加）
cum_return_stock = return_stock['portfolio'].cumsum()
cum_return_futures = return_futures.cumsum()  # 4个期货一起算
plt.figure(2, figsize=(16, 9))
plt.plot(data_stock['date'][1:], cum_return_stock, lw=2, label='投资组合')
plt.plot(data_stock['date'][1:], cum_return_futures['IF'], lw=2, label='IF沪深300期货')
plt.plot(data_stock['date'][1:], cum_return_futures['IH'], lw=2, label='IH上证50期货')
plt.plot(data_stock['date'][1:], cum_return_futures['IC'], lw=2, label='IC中证500期货')
plt.plot(data_stock['date'][1:], cum_return_futures['IM'], lw=2, label='IM中证1000期货')
plt.title("投资组合累积收益率", fontsize=32)
plt.xlabel("时间")
plt.ylabel("累计对数收益率")
plt.legend()
plt.savefig('投资组合累积收益率.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 开始进行回归计算最小方差套期保值比例
R_squared = []
# 沪深300IF
# x = return_stock.loc[:, ['portfolio']].values
# X = sm.add_constant(x)
# Y = return_futures.loc[:, ['IF']]
# model = sm.OLS(Y, X)
# results = model.fit()
# print(results.summary())
# R_squared.append(results.rsquared)

for i in range(return_futures.shape[1]):
    x = return_stock.loc[:, ['portfolio']].values
    X = sm.add_constant(x)
    Y = return_futures.iloc[:, i]
    model = sm.OLS(Y, X)
    results = model.fit()
    print(results.summary())
    R_squared.append(results.rsquared)
print(R_squared)

# 找到最大的R方及其对应的回归系数
best_futures_index = R_squared.index(max(R_squared))
print("回归效果最好的是"+str(return_futures.columns[best_futures_index]))
print("其回归系数为")
x = return_stock.loc[:, ['portfolio']].values
X = sm.add_constant(x)
Y = return_futures.iloc[:, best_futures_index]
model = sm.OLS(Y, X)
results = model.fit()
best_alpha = results.params[0]
best_beta = results.params[1]
print(best_beta)

# 以上得到了最小方差套期保值比例
# 下面计算卖空多少期货
multiplier = [300, 300, 200, 200]
invest = 100000000
v_IF = data_futures.iloc[-1, best_futures_index+1]*multiplier[best_futures_index]
print(v_IF)
N = best_beta*invest/v_IF
print("应当卖空"+f"{N:,.2f}"+"份"+str(return_futures.columns[best_futures_index])+"股指期货合约")

# 画出股票组合和股指期货收益率的散点图，同时画出两者的拟合直线
plt.figure(3, figsize=(16, 9))
plt.scatter(return_futures.iloc[:, best_futures_index], return_stock.iloc[:, -1])
# plt.show()
# print(return_futures.iloc[:, best_futures_index])
# print(return_stock.iloc[:, -1])
x_plot = np.linspace(-0.1, 0.1, 1001)
y_plot = best_alpha+best_beta*x_plot
plt.plot(x_plot, y_plot, 'r', lw=2, label=str(return_futures.columns[best_futures_index]))
plt.title("股票组合和股指期货收益率散点图及其拟合直线", fontsize=32)
plt.xlabel("股指期货收益率")
plt.ylabel("股票投资组合收益率")
plt.legend()
plt.text(-0.08, 0.08, "R^2="+str(max(R_squared)), fontsize=24)
plt.savefig('股票组合和股指期货收益率散点图及其拟合直线.jpg', dpi=300, bbox_inches='tight')
plt.show()