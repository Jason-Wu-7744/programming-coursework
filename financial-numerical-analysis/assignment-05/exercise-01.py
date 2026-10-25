# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
data = pd.read_excel('homework5_1_1.xlsx', index_col=0)
# print(data.shape)
# print(data)
data = data.drop(data.index[0], axis=0)
print(data.shape)
print(data)
#
# net_value190401 = data.iloc[1:2, :]
# net_value190402 = data.iloc[2:3, :]
# net_value190403 = data.iloc[3:4, :]
# net_value190404 = data.iloc[4:5, :]
# net_value190408 = data.iloc[5:6, :]
# net_value190409 = data.iloc[6:7, :]
# net_value190410 = data.iloc[7:8, :]
# net_value190411 = data.iloc[8:9, :]
# net_value190412 = data.iloc[9:10, :]
#
# # print(net_value190412)
# # net_value190412 = net_value190412.values
#
# list_net_value = [net_value190401, net_value190402, net_value190403, net_value190404, net_value190408, net_value190409, net_value190410, net_value190411, net_value190412]
#
# def net_value_sum(net_value_date):
#     sum = 0
#     net_value_date = net_value_date.values.astype(float)
#     for i in np.arange(net_value_date.size):
#         sum += net_value_date[0, i]
#     return sum
#
# # print(net_value_sum(net_value190412))
#
# dict_net_value_sum = {}
# for i in range(1, 10):
#     print(data.index[i])
#     dict_net_value_sum[data.index[i]] = net_value_sum(list_net_value[i-1])
# # print(dict_net_value_sum)
# pd_net_value_sum = pd.Series(dict_net_value_sum)
# print(pd_net_value_sum)
#
# dict_net_value_seperate190403 = {}
# for i in range(5):
#     dict_net_value_seperate190403[data.columns[i]] = data.values[3, i]
# # print(dict_net_value_seperate190403)
# pd_net_value_seperate190403 = pd.Series(dict_net_value_seperate190403)
# print(pd_net_value_seperate190403)
#以上为对于每个交易日的数据的求和，这不是题目所要求的，理解题目时出现了问题

arr_net_value_519606 = np.array(data.iloc[1:, 0])
print(arr_net_value_519606)
pd_net_value_519606 = pd.Series(arr_net_value_519606, index=data.index[1:])
print(pd_net_value_519606)

# print(data.index[1])

dict_net_value_seperate190403 = {}
for i in range(5):
    dict_net_value_seperate190403[data.columns[i]] = data.values[3, i]
# print(dict_net_value_seperate190403)
pd_net_value_seperate190403 = pd.Series(dict_net_value_seperate190403)
print(pd_net_value_seperate190403)

#第二小题
# pd_net_value_question2 = data.iloc[5:, 1:4]
# print(pd_net_value_question2)
#以上为直接通过iloc隐式截取了了一个新的表格，但题目要求先是一个数组

arr = np.array(data)
arr_net_value_question2 = arr[5:, 1:4]
print(arr_net_value_question2)
pd_net_value_question2 = pd.DataFrame(arr_net_value_question2, index=data.index[5:], columns=data.columns[1:4])
print(pd_net_value_question2)

#第三小题
data_withoutcode = data.drop('基金代码')
print(data_withoutcode)

#第四小题
list_net_value_519606 = list(pd_net_value_519606.values)
print(list_net_value_519606)

arr_net_value_seperate190403 = np.array(pd_net_value_seperate190403)
print(arr_net_value_seperate190403)

arr_net_value_question2 = np.array(pd_net_value_question2)
print(arr_net_value_question2)
