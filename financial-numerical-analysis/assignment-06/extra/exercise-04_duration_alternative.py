# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# data = pd.read_table(r'data/intertrade_ticks/600000_2007-01-04.txt', encoding='GB2312', sep=',')
# data.columns = ['time', 'price', 'change', 'volumn', 'amount', 'type']
# data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S')
# print(data)
#
# ind_morning = (data['time'] >= pd.to_datetime('09:30:00', format='%H:%M:%S')) & (data['time'] <= pd.to_datetime('11:30:00', format='%H:%M:%S'))
# time_morning = data.loc[ind_morning, 'time']
# print(time_morning)
# #.values把pandas变量变为数组，timedelta64把时间单位变为秒
# delta_time_morning = (time_morning.iloc[0:-1].values-time_morning.iloc[1:].values)/np.timedelta64(1, 's')
# print(delta_time_morning)
#
# ind_afternoon = (data['time'] >= pd.to_datetime('13:00:00', format='%H:%M:%S')) & (data['time'] <= pd.to_datetime('15:00:00', format='%H:%M:%S'))
# time_afternoon = data.loc[ind_afternoon, 'time']
# print(time_afternoon)
# delta_time_afternoon = (time_afternoon.iloc[0:-1].values-time_afternoon.iloc[1:].values)/np.timedelta64(1, 's')
# print(delta_time_afternoon)
#
# delta_time_day = np.concatenate((delta_time_morning, delta_time_afternoon), axis=0)
# print(delta_time_day)
#
# plt.figure(1)
# # 只给 plt.plot() 一个一维数组时，matplotlib 会把它当成 y 值，并自动用 0, 1, 2, … 作为对应的 x 值（即索引序列）画图。
# plt.plot(delta_time_day)
# plt.show()
#以上为一天的情况
#多日数据：

date_range = pd.date_range('2007-01-04', '2007-01-31', freq='D')
print(date_range)
delta_time = []
for day in date_range:
    print(str(day))
    if os.path.exists(r'data/intertrade_ticks/600000_'+str(day)[:10]+'.txt'):
        data = pd.read_table(r'data/intertrade_ticks/600000_'+str(day)[:10]+'.txt', encoding='GB2312', sep=',')
        data.columns = ['time', 'price', 'change', 'volumn', 'amount', 'type']
        data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S')
        # print(data)

        ind_morning = (data['time'] >= pd.to_datetime('09:30:00', format='%H:%M:%S')) & (data['time'] <= pd.to_datetime('11:30:00', format='%H:%M:%S'))
        time_morning = data.loc[ind_morning, 'time']
        # print(time_morning)
        #.values把pandas变量变为数组，timedelta64把时间单位变为秒
        delta_time_morning = (time_morning.iloc[0:-1].values-time_morning.iloc[1:].values)/np.timedelta64(1, 's')
        # print(delta_time_morning)

        ind_afternoon = (data['time'] >= pd.to_datetime('13:00:00', format='%H:%M:%S')) & (data['time'] <= pd.to_datetime('15:00:00', format='%H:%M:%S'))
        time_afternoon = data.loc[ind_afternoon, 'time']
        # print(time_afternoon)
        delta_time_afternoon = (time_afternoon.iloc[0:-1].values-time_afternoon.iloc[1:].values)/np.timedelta64(1, 's')
        # print(delta_time_afternoon)

        delta_time_day = np.concatenate((delta_time_morning, delta_time_afternoon), axis=0)
        print(delta_time_day)
        print(len(delta_time_day))

        if len(delta_time) == 0:
            delta_time = delta_time_day
        else:
            delta_time = np.concatenate((delta_time, delta_time_day), axis=0)

print(len(delta_time))
# plt.figure(2)
# plt.plot(delta_time)
# plt.show()


#下面开始二分法数值求根，但是得先构造极大似然函数
def equation_theta(theta, delta_time):
    n = len(delta_time)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += np.log(1+theta*delta_time[i])
        sum2 += delta_time[i]/(1+theta*delta_time[i])
    f_theta = n/theta - (1+n/sum1)*sum2
    return f_theta

# theta_plot = np.arange(0, 0.02, 0.00001)
# f_theta_plot = equation_theta(theta_plot, delta_time)
# plt.figure(3)
# plt.plot(theta_plot, f_theta_plot)
# plt.show()

def rootfinding_bisection(a, b, e):
    c = (a+b)/2
    while b-c > e:
        sign_fa = np.sign(equation_theta(a, delta_time))
        sign_fb = np.sign(equation_theta(b, delta_time))
        sign_fc = np.sign(equation_theta(c, delta_time))
        if sign_fb*sign_fc <= 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
    return c

print('theta:', rootfinding_bisection(0.01, 0.02, 10**(-6)))
theta = rootfinding_bisection(0.01, 0.02, 10**(-6))

sum1 = 0
n = len(delta_time)
for i in range(n):
    sum1 += np.log(1+theta*delta_time[i])
beta = n/sum1
print("beta:", beta)

mu = theta*beta
q = 1+ 1/beta
print("mu:", mu)
print("q:", q)
