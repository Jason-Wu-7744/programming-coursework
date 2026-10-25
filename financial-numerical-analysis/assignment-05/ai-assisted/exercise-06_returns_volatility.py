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

#第一小题
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
#
# def volatility_for_series(data):
#     s = 0
#     for i in range(data.shape[0]):
#         rday = earning(data.iloc[i, 0], data.iloc[i-1, 0])
#         s += rday**2
#     return np.sqrt(s)
# print(volatility_for_series(data_close))
#
yearly_return = []
for i in range(first_day.shape[0]):
    yearly_return.append(earning(first_day.iloc[i, 0], last_day.iloc[i, 0]))
# print(yearly_return)
#
# yearly_volatility = []
# for i in range(data_close.shape[0]):
#     a2005, a2006, a2007, a2008, a2009, a2010, a2011, a2012, a2013, a2014, a2015, a2016, a2017, a2018 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#     if data_close.index[i] <= last_day[0]:
#         a2005 += volatility_for_series(data_close)
#     elif data_close.index[i] <= last_day[1]:
#用非sql的方法实在是极为繁琐

log_ret = np.log(data_close/data_close.shift(1))
#.shift(1)往下一行
annual_vol = (
    log_ret.groupby(log_ret.index.year)
           .apply(lambda r: np.sqrt(np.sum(r**2, axis=0))))
# print(annual_vol)

for i in range(2005, 2019):
    print(i, ", Yearly Return:"+str(yearly_return[i-2005]*100)+"%, Yearly Volatility:"+str(annual_vol.iloc[i-2005, 0]*100)+"%")
