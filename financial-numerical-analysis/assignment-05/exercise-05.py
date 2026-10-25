# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
data = pd.read_csv('Exp05-Python-实验数据-第5题.csv', encoding='GB2312', index_col= 0)
# print(data)

list_index1 = []
list_time1 = []
list_index2 = []
list_time2 = []
list_index3 = []
list_time3 = []


for i in range(data.shape[0]):
    if data.index[i] == "恒生指数":
        list_index1.append(data.iloc[i, 1])
        list_time1.append(data.iloc[i, 0])
    elif data.index[i] == "西班牙马德里指数":
        list_index2.append(data.iloc[i, 1])
        list_time2.append(data.iloc[i, 0])
    elif data.index[i] == "土耳其ISE-N100指数":
        list_index3.append(data.iloc[i, 1])
        list_time3.append(data.iloc[i, 0])

data_1 = pd.Series(list_index1, index=pd.to_datetime(list_time1, format='%Y/%m/%d'))
# print(data_1)
data_2 = pd.Series(list_index2, index=pd.to_datetime(list_time2, format='%Y/%m/%d'))
# print(data_2)
data_3 = pd.Series(list_index3, index=pd.to_datetime(list_time3, format='%Y/%m/%d'))
# print(data_3)

data_combined = pd.concat([data_1, data_2, data_3], axis=1, join='outer')
data_combined.columns = ["恒生指数", "西班牙马德里指数", "土耳其ISE-N100指数"]
print(data_combined)

for i in range(data_combined.shape[1]):
    if data_combined.iloc[:, i].isnull().sum() == 0:
        print(data_combined.columns[i], "无缺失值")
    else:
        s = 0
        for a in range(data_combined.shape[0]):
            if pd.isna(data_combined.iloc[a, i]):
                s += 1
                print(data_combined.columns[i], "的", data_combined.index[a], "缺失/第", a+1, "行缺失")
        print(data_combined.columns[i], "缺失了", s, "个值")

# print(data_combined.isnull())

#第二小题
data_dropped = pd.DataFrame.dropna(data_combined, axis=0)
print(data_dropped.shape, data_combined.shape)
for i in range(data_dropped.shape[1]):
    if data_dropped.iloc[:, i].isnull().sum() == 0:
        print(data_dropped.columns[i], "无缺失值")
    else:
        s = 0
        for a in range(data_dropped.shape[0]):
            if pd.isna(data_dropped.iloc[a, i]):
                s += 1
                print(data_dropped.columns[i], "的", data_dropped.index[a], "缺失/第", a+1, "行缺失")
        print(data_dropped.columns[i], "缺失了", s, "个值")

#第三小题
# data_filled = data_combined.fillna(method='ffill', axis=0)
data_filled = data_combined.ffill()
print(data_filled)

#第四小题
# data_filled = data_combined.fillna(method='bfill', axis=0)
data_filled = data_combined.bfill()
print(data_filled)