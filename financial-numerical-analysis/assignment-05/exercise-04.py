# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
data600004 = pd.read_excel('exercise-04_白云机场.xlsx', index_col=0)
data600011 = pd.read_excel('exercise-04_华能国际.xlsx', index_col=0)
data600029 = pd.read_excel('exercise-04_南方航空.xlsx', index_col=0)
data600031 = pd.read_excel('exercise-04_三一重工.xlsx', index_col=0)
data600158 = pd.read_excel('exercise-04_中体产业.xlsx', index_col=0)

data = pd.concat([data600004, data600011, data600029, data600031, data600158], axis=1, keys=['白云机场', '华能国际', '南方航空', '三一重工', '中体产业'])
data.columns = ['白云机场', '华能国际', '南方航空', '三一重工', '中体产业']
data.index = pd.to_datetime(data.index, format='%Y-%m-%d')
#原来导入的index只是时间文本
# print(data)
print(data.index)
print(data.columns)
print(data.shape)

#第二小题
# data_200408 = data.loc[pd.to_datetime('2020-04-08', format='%Y-%m-%d'), :]
# print(data_200408)
#
# data_200516 = data.loc[pd.to_datetime('2020-05-16', format='%Y-%m-%d'), :]
# print(data_200516)

compound_growth_turtle_date = ['2020-04-08', '2020-05-16', '2020-06-10']
def date_data(date):
    if date in data.index:
        return data.loc[pd.to_datetime(date, format='%Y-%m-%d')]
    else:
        return str(date)+"不交易"

for i in compound_growth_turtle_date:
    print(i, "数据如下:")
    print(date_data(i))

for i in data.index:
    if i >= pd.to_datetime('2020-06-15', format='%Y-%m-%d') and i <= pd.to_datetime('2020-06-19', format='%Y-%m-%d'):
        print(i, "数据如下:")
        print(date_data(i))

#第三小题
data_question3 = data.iloc[15:28, 1:4]
print(data_question3)

#第四小题
data_question4_1 = data[data['白云机场'] >= 17.6]
data_question4_1 = data_question4_1['白云机场']
print(data_question4_1)

data_question4_2 = data[(data['华能国际'] <= 6.6) & (data['南方航空'] > 7.5) & (data['三一重工'] < 12.9)]
print(data_question4_2)
#data用于列索引更为合适
# 用&而非and，注意加()