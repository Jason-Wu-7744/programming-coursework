# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Earlier source version retained for coursework history.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})
# 读取数据
data = scipy.io.loadmat('Exp07-Python-实验数据-TickReturn.mat')
print(data)
# scipy.io.loadmat读出来的mat文件是一个字典
data = data['r']
print(data)
data = pd.DataFrame(data)
data.columns = ['r']
print(data)
# print(len(data))
print(max(data['r']))
print(min(data['r']))

# 标准地分割区间
bins = np.linspace(-0.1, 0.1, 101)
print(len(bins))
labels = []
for i in range(100):
    labels.append(i+1)
print(labels)
data['group'] = pd.cut(data['r'], bins=bins, labels=labels)
print(data)

group_counts = data.groupby('group', observed=False).size()
print(group_counts)
group_counts = pd.DataFrame(group_counts, columns=['group'])
print(group_counts)

#算r，p以便回归和画图
freq = []
delta_lin = bins[1]-bins[0]
for i in range(len(group_counts['group'])):
    p = group_counts.iloc[i, 0]/delta_lin/len(data['r'])
    freq.append(p)
print(freq)
print(len(freq))

bins_x_axis = []
for i in range(1, len(bins)):
    x_axis = (bins[i]+bins[i-1])/2
    bins_x_axis.append(x_axis)

#整理数据
group_counts['r'] = bins_x_axis
group_counts['p'] = freq
print(group_counts)

#回归
# n = len(group_counts['r'])
# sum_x = np.sum(np.log(group_counts['r']))
# sum_y = np.sum(np.log(group_counts['p']))
#
# sum_x_sqr = 0
# sum_xy = 0
# for i in np.log(np.abs(group_counts['r'])):
#     sum_x_sqr += i**2
# for i in range(n):
#     sum_xy += np.log(np.abs(group_counts['r'][i]))*np.log(group_counts['p'][i])
#
# A = np.array([[n, sum_xy],
#               [sum_xy, sum_x_sqr]
#               ])
# print(A)
# b = np.array([[sum_y],
#               [sum_xy]
#               ])
# print(b)
# x = np.dot(np.linalg.inv(A), b)
# # # 这里出现了一个重要的问题，有的p<0，不能取对。这道题只能用取对数来回归，所以只能删去p为0的数据
# print(x)
#
# x_show = np.arange(-0.1, 0.1, 0.0001)
# y_show = x[1, 0]*x_show+x[0, 0]
# print(y_show)

#下面开始删去0数据
x_data = []
y_data = []
for i in range(len(group_counts['r'])):
    if group_counts.iloc[i, 2] != 0:
        x_data.append(np.log(np.abs(group_counts.iloc[i, 1])))
        y_data.append(np.log(group_counts.iloc[i, 2]))
print(x_data)
print(len(x_data))
print(y_data)
print(len(y_data))

#根据整理好的没有0的数据再次回归
n = len(x_data)
sum_x = np.sum(x_data)
sum_y = np.sum(y_data)

sum_xx = 0
sum_xy = 0
for i in x_data:
    sum_xx += i**2
for i in range(n):
    sum_xy += x_data[i]*y_data[i]
A = np.array([[n, sum_xy],
              [sum_xy, sum_xx]
              ])
b = np.array([[sum_y],
              [sum_xy]
              ])
x = np.dot(np.linalg.inv(A), b)
print(x)

#画图
x_show = np.arange(-0.1, 0.1, 0.001)
y_show = np.e**x[0, 0]*np.abs(x_show)*(np.e**x[1, 0])


plt.figure(1)
plt.scatter(bins_x_axis, freq)
plt.loglog(x_show, y_show)
# 把y轴变为对数表示
plt.yscale('log')
plt.yticks(np.logspace(-4, 4, 5))
plt.show()



# 对数分割区间（需要区分正负）