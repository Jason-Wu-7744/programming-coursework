# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
#数据库：保存的ipv4/端口-数据库-表-主键


mysql_config = {
    'host': os.environ['FNA_DB_HOST'],
    'port': int(os.environ['FNA_DB_PORT']),
    'user': os.environ['FNA_DB_USER'],
    'password': os.environ['FNA_DB_PASSWORD'],
    'dbname': os.environ['FNA_DB_NAME'],
}
mysql_engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(**mysql_config), pool_pre_ping=True)
#用sql写从哪张表的哪一个主键（普通键的条件也可以加）导入哪些健的数据
sql = "select Date, Close From stock_trading_data where stkcd='002444' and Date Between '2016-01-01' and '2018-12-31';"
#read_sql两个要素：sql哪些数据、mysql_engine引擎
data = pd.read_sql(sql, mysql_engine)
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
# data.index = data['Date']
# data = data.drop('Date', axis=1)
print(data)

# #考虑到index可以直接index，ddate作为索引更为合适
# first_day = data.groupby(data.index.year).head(1)
# last_day = data.groupby(data.index.year).tail(1)
# print(first_day)
# print(last_day)

#第一小题
data_annual_head = data.groupby(data['Date'].dt.year).head(1)
data_annual_tail = data.groupby(data['Date'].dt.year).tail(1)
print(data_annual_head)
print(data_annual_tail)
print(data_annual_tail.shape)

yield_annual = []
for i in range(data_annual_tail.shape[0]):
    a = np.log(data_annual_tail.iloc[i, 1])-np.log(data_annual_head.iloc[i, 1])
    yield_annual.append(a)
print(yield_annual)

vol_daily = {}
for i in range(data.shape[0]-1):
    a = np.log(data.iloc[i+1, 1]/data.iloc[i, 1])**2
    vol_daily[data.iloc[i+1, 0]] = a
# print(vol_daily)

vol_daily = pd.Series(vol_daily)
print(vol_daily)
vol_annual_sum = np.sqrt(vol_daily.groupby(vol_daily.index.year).sum())
print(vol_annual_sum)

for i in range(len(yield_annual)):
    print(vol_annual_sum.index[i], ", Yearly Return:", yield_annual[i]*100, "%, Yearly Volatility:", vol_annual_sum.iloc[i]*100, "%")



#第二小题
mu = np.mean(yield_annual)
sigma = np.mean(vol_annual_sum.iloc[:])
print(mu, sigma)

price_head_2019 = data.iloc[-1, 1]
print(price_head_2019)
#数据库中没有2019年的交易数据，所以只能用没有周末的时间序列来代替
weekdays = pd.bdate_range('2019-01-01', '2019-06-30')
dt = 0.5/len(weekdays)
#模拟的步长（一天）
print(dt)

#一个循环be like
# price = []
# ln_p = np.log(price_head_2019)
# for i in range(len(weekdays)):
#     ln_p += delta_ln_p[i]
#     price.append(np.e**ln_p)
# print(price)
# print(len(price))

price_sim = []
for a in range(5):
    epsilon = np.random.normal(0, 1, size=len(weekdays))
    dw = epsilon * np.sqrt(dt)
    print(dw)
    delta_ln_p = (mu - sigma ** 2 / 2) * dt + sigma * dw
    print(delta_ln_p)
    print(len(weekdays))
    print(len(delta_ln_p))
    ln_p = np.log(price_head_2019)
    price = []
    for i in range(len(weekdays)):
        ln_p += delta_ln_p[i]
        price.append(np.e**ln_p)
    price_sim.append(price)
print(price_sim)

#接着把一个长度为5的列表，列表的每一个元素为长度为129的列表，如何把它变为一个129行，5列的dataframe
#用到转置
price_txt = pd.DataFrame(price_sim).T
print(price_txt)
# price_txt['Date'] = pd.bdate_range('2019/01/01', '2019/06/30')
price_txt.insert(0, 'Date', pd.bdate_range('2019/01/01', '2019/06/30'))
print(price_txt)

price_txt.columns = ['date', 'close_sim 1', 'close_sim 2', 'close_sim 3', 'close_sim 4', 'close_sim 5']
print(price_txt)

close_price = pd.read_excel('price_002444.xlsx')
close_price.columns = ['date', 'close_price']
close_price['date'] = pd.to_datetime(close_price['date'], format='%Y-%m-%d')
print(close_price)

#外连接合并
price_txt = pd.merge(close_price, price_txt, on='date', how='outer')
print(price_txt)
#查找缺失值
print(price_txt.isnull().sum())
#补上
price_txt = price_txt.bfill()
print(price_txt.isnull().sum())
price_txt = price_txt.dropna()
print(price_txt.isnull().sum())
print(price_txt)

#开始存入txt
with open('exercise-06_monte_carlo_alternative.txt', 'w') as f:
    f.write('date\tclose_price\tclose_sim 1\tclose_sim 2\tclose_sim 3\tclose_sim 4\tclose_sim 5\n')
    for i in range(price_txt.shape[0]):
        f.write(price_txt.iloc[i, 0].strftime('%Y/%m/%d'))
        #f.write默认不换行
        f.write('\t'+str(f'{price_txt.iloc[i, 1]:.2f}'))
        f.write('\t'+str(f'{price_txt.iloc[i, 2]:.2f}'))
        f.write('\t'+str(f'{price_txt.iloc[i, 3]:.2f}'))
        f.write('\t'+str(f'{price_txt.iloc[i, 4]:.2f}'))
        f.write('\t'+str(f'{price_txt.iloc[i, 5]:.2f}'))
        f.write('\t'+str(f'{price_txt.iloc[i, 6]:.2f}')+'\n')





#第三小题
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data_plt = pd.read_table('exercise-06_monte_carlo_alternative.txt')
data_plt['date'] = pd.to_datetime(data_plt['date'], format='%Y/%m/%d')
print(data_plt)

plt.figure(1)
# plt.plot(data['Date'], data['Close'])
#可以发现一个很有启发性的现象，由于2016至2018贸易战期间巨星科技的股价表现实在太差， 由历史数据推出来mu和sigma导致了后续推断数据继续向下，且波动不大
plt.plot(data_plt['date'], data_plt['close_price'], '-k', lw=2)
plt.plot(data_plt['date'], data_plt['close_sim 1'], lw=1.5)
plt.plot(data_plt['date'], data_plt['close_sim 2'], lw=1.5)
plt.plot(data_plt['date'], data_plt['close_sim 3'], lw=1.5)
plt.plot(data_plt['date'], data_plt['close_sim 4'], lw=1.5)
plt.plot(data_plt['date'], data_plt['close_sim 5'], lw=1.5)

plt.xlabel(r'$t$', fontname='Times New Roman', fontsize='34')
plt.ylabel(r'$p(t)$', fontname='Times New Roman', fontsize='34')

plt.xticks(ticks=pd.to_datetime(['2019-01-15', '2019-02-15', '2019-03-15', '2019-04-15', '2019-05-15', '2019-06-15']),
           labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
           fontsize=26,
           fontname='Times New Roman')
plt.yticks(ticks=np.linspace(7, 13, 5),
           fontsize=26,
           fontname='Times New Roman')
plt.legend(['real price'], loc='upper left', fontsize=26)


plt.savefig('exercise-06_rxtra.jpg', dpi=300, bbox_inches='tight')
plt.show()