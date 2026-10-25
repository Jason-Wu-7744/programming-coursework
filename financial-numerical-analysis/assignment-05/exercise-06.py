# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
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

sql = "SELECT Stkcd, Name, Date, Open, High, Low, Close FROM stock_trading_data WHERE Stkcd='000021';"
#一条 SQL 查询语句
data = pd.read_sql(sql, mysql_engine)
#pandas 把这条 SQL 送到刚才建好的数据库引擎

print(data.head())
#把 DataFrame 的前 5 行打印出来
print(data.tail())

#第一小题
sql = "SELECT Date, Close FROM stock_trading_data WHERE Stkcd='000001' AND Date BETWEEN '2005-01-01' AND '2019-12-31';"
#运用and添加条件
data_close = pd.read_sql(sql, mysql_engine, index_col='Date')
print(data_close)