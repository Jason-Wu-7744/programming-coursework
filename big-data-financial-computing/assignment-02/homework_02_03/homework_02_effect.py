import numpy as np
import pandas as pd

# 选取2000下半年上市的5只股票作为研究对象
data_600016 = pd.read_excel('600016.xlsx')
data_600016.columns = ['date', 'return1']
data_600016['date'] = pd.to_datetime(data_600016['date'])
print(data_600016)
data_600019 = pd.read_excel('600019.xlsx')
data_600019.columns = ['date', 'return2']
data_600019['date'] = pd.to_datetime(data_600019['date'])
print(data_600019)
data_600276 = pd.read_excel('600276.xlsx')
data_600276.columns = ['date', 'return3']
data_600276['date'] = pd.to_datetime(data_600276['date'])
print(data_600276)
data_600316 = pd.read_excel('600316.xlsx')
data_600316.columns = ['date', 'return4']
data_600316['date'] = pd.to_datetime(data_600316['date'])
print(data_600316)
data_600320 = pd.read_excel('600320.xlsx')
data_600320.columns = ['date', 'return5']
data_600320['date'] = pd.to_datetime(data_600320['date'])
print(data_600320)

data = pd.concat([data_600016, data_600019['return2'], data_600276['return3'], data_600316['return4'], data_600320['return5']], axis=1).ffill()
print(data)

# N=M=1时
max_return_1 = []
min_return_1 = []
for i in range(299):
    min_code = data.iloc[i, 1:].idxmin()
    # print(min_code)
    max_code = data.iloc[i, 1:].idxmax()
    min_return_1.append(data.loc[i+1, min_code])
    max_return_1.append(data.loc[i+1, max_code])
print(min_return_1)
print(sum(min_return_1)/len(min_return_1))
print(max_return_1)
print(sum(max_return_1)/len(max_return_1))
print(sum(max_return_1)/len(max_return_1)-sum(min_return_1)/len(min_return_1))
# 1月短期反转效应存在


# N=M=3时
max_return_3 = []
min_return_3 = []
for i in range(2, 296, 3):
    min_code = ((1+data.iloc[i-2, 1:])*(1+data.iloc[i-1, 1:])*(1+data.iloc[i, 1:])-1).idxmin()
    # print(min_code)
    max_code = ((1+data.iloc[i-2, 1:])*(1+data.iloc[i-1, 1:])*(1+data.iloc[i, 1:])-1).idxmax()
    min_return_3.append((1+data.loc[i+1, min_code])*(1+data.loc[i+2, min_code])*(1+data.loc[i+3, min_code])-1)
    max_return_3.append((1+data.loc[i+1, min_code])*(1+data.loc[i+2, min_code])*(1+data.loc[i+3, max_code])-1)
print(min_return_3)
print(sum(min_return_3)/len(min_return_3))
print(max_return_3)
print(sum(max_return_3)/len(max_return_3))
print(sum(max_return_3)/len(max_return_3)-sum(min_return_3)/len(min_return_3))
# 3月短期反转效应存在


# N=M=6时
max_return_6 = []
min_return_6 = []
# 定义计算n期累积收益率的lambda函数
calc_cum_ret = lambda start_idx, length: (1 + data.iloc[start_idx:start_idx + length, 1:]).prod() - 1
calc_port_ret = lambda code, start_idx, length: (1 + data.loc[start_idx:start_idx + length - 1, code]).prod() - 1
# prod表连乘
for i in range(5, 294, 6):
    form_ret = calc_cum_ret(i - 5, 6)
    min_code = form_ret.idxmin()
    max_code = form_ret.idxmax()
    min_return_6.append(calc_port_ret(min_code, i + 1, 6))
    max_return_6.append(calc_port_ret(max_code, i + 1, 6))
print(min_return_6)
print(sum(min_return_6) / len(min_return_6))
print(max_return_6)
print(sum(max_return_6) / len(max_return_6))
print(sum(max_return_6) / len(max_return_6)-sum(min_return_6) / len(min_return_6))
# 6月惯性效应存在


# N=M=12时
max_return_12 = []
min_return_12 = []
for i in range(11, 288, 12):
    form_ret = calc_cum_ret(i - 11, 12)
    min_code = form_ret.idxmin()
    max_code = form_ret.idxmax()
    min_return_12.append(calc_port_ret(min_code, i + 1, 12))
    max_return_12.append(calc_port_ret(max_code, i + 1, 12))
print(min_return_12)
print(sum(min_return_12) / len(min_return_12))
print(max_return_12)
print(sum(max_return_12) / len(max_return_12))
print(sum(max_return_12) / len(max_return_12)-sum(min_return_12) / len(min_return_12))
# 12月惯性效应存在

