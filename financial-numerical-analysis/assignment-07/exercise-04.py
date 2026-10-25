# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
#数据库：保存的ipv4/端口-数据库-表-主键
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

mysql_config = {
    'host': os.environ['FNA_DB_HOST'],
    'port': int(os.environ['FNA_DB_PORT']),
    'user': os.environ['FNA_DB_USER'],
    'password': os.environ['FNA_DB_PASSWORD'],
    'dbname': os.environ['FNA_DB_NAME'],
}
mysql_engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(**mysql_config), pool_pre_ping=True)
#用sql写从哪张表的哪一个主键（普通键的条件也可以加）导入哪些健的数据
sql = "select Date, Close From stock_trading_data where stkcd='000002' and Date Between '2010-01-01' and '2018-12-31';"
#read_sql两个要素：sql哪些数据、mysql_engine引擎
data_000002 = pd.read_sql(sql, mysql_engine)
data_000002['Date'] = pd.to_datetime(data_000002['Date'], format='%Y-%m-%d')
print(data_000002)

# data_000300 = pd.read_sql(sql, mysql_engine)
# data_000300['Date'] = pd.to_datetime(data_000300['Date'], format='%Y-%m-%d')
# print(data_000300)
# 数据库中似乎没有指数，从resset中读取

data_000300 = pd.read_excel('000300_2010_2018.xlsx')
data_000300.columns = ['Date', 'Close']
data_000300['Date'] = pd.to_datetime(data_000300['Date'], format='%Y-%m-%d')
print(data_000300)

#用DR001作为无风险利率
data_DR001 = pd.read_excel('DR001_2010_2018.xlsx')
data_DR001.columns = ['Date', 'Base']
data_DR001['Date'] = pd.to_datetime(data_DR001['Date'], format='%Y-%m-%d')
print(data_DR001)
data_DR001['Base'] = data_DR001['Base']/100/360
print(data_DR001)


#下面开始算收益率
data_000002_yield = []
for i in range(1, len(data_000002['Date'])):
    data_000002_yield.append((data_000002['Close'][i] - data_000002['Close'][i-1])/data_000002['Close'][i-1])
data_000002_yield.insert(0, 0)
print(data_000002_yield)
data_000002['Yield_000002'] = data_000002_yield
print(data_000002)

data_000300_yield = []
for i in range(1, len(data_000300['Date'])):
    data_000300_yield.append((data_000300['Close'][i] - data_000300['Close'][i-1])/data_000300['Close'][i-1])
data_000300_yield.insert(0, 0)
print(data_000300_yield)
data_000300['Yield_000300'] = data_000300_yield
print(data_000300)

yield_000002 = data_000002.drop(columns=['Close'])
print(yield_000002)
yield_000300 = data_000300.drop(columns=['Close'])
print(yield_000300)

yield_stock = pd.merge(yield_000002, yield_000300, on='Date', how='outer')
print(yield_stock)
yield_ols = pd.merge(yield_stock, data_DR001, on='Date', how='inner')
print(yield_ols)

#检查遗漏数据
print(yield_ols.isnull().sum())
#幸运地是没有遗漏数据，但是需要去掉第一行
yield_ols = yield_ols.drop(index=0).reset_index(drop=True)
print(yield_ols)

#计算超额收益率
excess_000002 = yield_ols['Yield_000002'] - yield_ols['Base']
excess_000300 = yield_ols['Yield_000300'] - yield_ols['Base']
yield_ols['excess_000002'] = excess_000002
yield_ols['excess_000300'] = excess_000300
print(yield_ols)

#开始回归
n = len(yield_ols['Date'])

sum_x = np.sum(yield_ols['excess_000300'])
sum_y = np.sum(yield_ols['excess_000002'])
print(sum_x, sum_y, n)


sum_xx = 0
for i in yield_ols['excess_000300']:
    sum_xx += i**2
print(sum_xx)

sum_xy = 0
for i in range(n):
    sum_xy += yield_ols.iloc[i, 4]*yield_ols.iloc[i, 5]
print(sum_xy)

A = np.array([[n, sum_x], [sum_x, sum_xx]])
print(A)
b = np.array([[sum_y], [sum_xy]])
print(b)

x = np.dot(np.linalg.inv(A), b)
print(x)

print("斜率：", x[1, 0])
print("截距", x[0, 0])

plt.figure(1)
plt.scatter(yield_ols['excess_000300'], yield_ols['excess_000002'], s=2)
x_plot = np.arange(-0.1, 0.1, 0.0001)
y_plot = x[1, 0]*x_plot + x[0, 0]
plt.plot(x_plot, y_plot, "-r")
plt.legend(['real value', 'fitted value'])
plt.xlabel(r"$excess yield 000300$")
plt.ylabel(r"$excess yield 000002$")
plt.savefig('exercise-04.jpg', dpi=600, bbox_inches='tight')
plt.show()

# 讨论：
# 可以看到，图中大多数点集中在中心区域，这表明大多数交易日股票的收益率数值较为稳定。
# 图中可以看到y=0处的点很多，这可能是因为数据库中把万科A没有交易的交易日的收盘价标为与上一日相同导致的，这也是为什么在数据检漏的过程中没有发现遗漏的原因。
# 图中点的纵坐标限制在了正负0.1之间，这是涨跌停版的作用。
# 拟合出的曲线斜率为0.9256，表明指数每上涨一个点，万科A就会平均上涨0.9256个点。这个CAPM中的β值<1，与万科价值而非成长的股票属性相符。
