# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Explicit AI-assisted source version; not claimed as independent work.
import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

mysql_config = {
    'host': os.environ['FNA_DB_HOST'],
    'port': int(os.environ['FNA_DB_PORT']),
    'user': os.environ['FNA_DB_USER'],
    'password': os.environ['FNA_DB_PASSWORD'],
    'dbname': os.environ['FNA_DB_NAME'],
}
#定义数据库信息字典以便后续调用

mysql_engine = create_engine(
    'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(**mysql_config),
    pool_pre_ping=True)
#创建数据库“引擎”对象

sql = "SELECT Date, Close FROM stock_trading_data WHERE Stkcd='000021' AND Date BETWEEN '2005-01-01' AND '2018-12-31';"
#运用and添加条件
data_close = pd.read_sql(sql, mysql_engine, index_col='Date')
# print(data_close)

first_day = data_close.groupby(data_close.index.year).head(1)
# print(first_day)
last_day = data_close.groupby(data_close.index.year).tail(1)
# print(last_day)

def earning(a, b):
    c = np.log(b) - np.log(a)
    return c

yearly_return = []
for i in range(first_day.shape[0]):
    yearly_return.append(earning(first_day.iloc[i, 0], last_day.iloc[i, 0]))

log_ret = np.log(data_close/data_close.shift(1))
#.shift(1)往下一行
annual_vol = (
    log_ret.groupby(log_ret.index.year)
           .apply(lambda r: np.sqrt(np.sum(r**2, axis=0))))
# print(annual_vol)


#第二小题
mu = np.mean(yearly_return)
sigma = annual_vol.mean()
#正是把日对数收益率按年加总再开方，数学上恰好等于连续复利收益率的年化标准差

sql0 = "SELECT Close FROM stock_trading_data WHERE Stkcd='000021' AND Date='2018-12-28';"
p0 = pd.read_sql(sql0, mysql_engine).iloc[0, 0]

calendar = pd.bdate_range('2019-01-01', '2019-06-28')
n_days = len(calendar)
dt = 0.5 / n_days

def sim_path(mu, sigma, p_start, n, dt):
    ln_p = np.log(p_start)
    prices = []
    for _ in range(n):
        eps = np.random.normal()
        dln_p = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * eps
        ln_p += dln_p
        prices.append(np.exp(ln_p))
    return prices

sim_prices = np.array([sim_path(mu, sigma, p0, n_days, dt) for _ in range(5)])



real_sql = """
SELECT Date, Close
FROM stock_trading_data
WHERE Stkcd='000021' AND Date BETWEEN '2019-01-01' AND '2019-06-30';
"""
real_df = pd.read_sql(real_sql, mysql_engine, parse_dates=['Date'])
real_df = real_df.set_index('Date').reindex(calendar)
real_df = real_df.ffill()
# print(real_df)


real_arr = real_df['Close'].astype(float).values

with open('MCSimulation_Jason_000021.txt', 'w') as f:
    f.write('date\tclose_price\tclose_sim 1\tclose_sim 2\tclose_sim 3\tclose_sim 4\tclose_sim 5\n')
    for i, day in enumerate(calendar):
        row = [day.strftime('%Y/%m/%d'), f'{real_arr[i]:.2f}'] + \
              [f'{sim_prices[k][i].item():.2f}' for k in range(5)]
        f.write('\t'.join(row) + '\n')

print('完成：sim_2019H1_000021.txt')