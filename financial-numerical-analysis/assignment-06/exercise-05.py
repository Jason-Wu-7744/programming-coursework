# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

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

m = len(delta_time)
print(m)

#化为pandas变量
delta_time = pd.DataFrame(delta_time, columns=['interval'])
print(delta_time)

#通过画图判断间隔如何划分
# plt.plot(delta_time)
# plt.show()

#分组
bins = np.logspace(0, 3, 11)
print(bins)
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
delta_time['group'] = pd.cut(delta_time['interval'], bins=bins, labels=labels)
print(delta_time)

group_counts = delta_time.groupby('group', observed=False).size()
group_counts = pd.DataFrame(group_counts, columns=['group'])
print(group_counts)

#计算每组频率
freq = []
for i in range(group_counts.shape[0]):
    if i == 0:
        base_i = bins[i]
    else:
        base_i = (bins[i] - bins[i-1])
    freq_i = group_counts.iloc[i, 0]/base_i/m
    freq.append(freq_i)
print(freq)
print(len(freq))
group_counts['freq'] = freq
print(group_counts)

x_spots = []
for i in range(1, len(bins)):
    a = (bins[i]+bins[i-1])/2
    x_spots.append(a)
print(x_spots)
print(len(x_spots))

#映射频率
plt.figure(1)
plt.loglog(x_spots, group_counts['freq'], 'sk', ms=11)
#画出拟合曲线
theta = 0.011138305664062497
beta = 8.802636157710321
mu = 0.09804645217410621
q = 1.1136023325380875
x = np.logspace(0, 2.6, 1000)
y = mu*(1+(1-q)*(-mu*x))**(q/(1-q))
plt.loglog(x, y, '-r', lw=2)
plt.legend(['Emp PDF', 'Fit $q$-exp'], loc='upper right', fontsize=15)
#图例似乎没有办法调整字体，这里为了不遮挡内容将图例字体缩小为15
plt.xlabel(r"$τ$", fontsize=36, fontname="Times New Roman")
plt.ylabel(r"$P(τ)$", fontsize=36, fontname="Times New Roman")
plt.xticks(fontsize=36, fontname="Times New Roman")
plt.yticks(ticks=np.logspace(0, -8, 5), fontsize=36, fontname="Times New Roman")

plt.savefig('exercise-05.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-05.jpg', dpi=300, bbox_inches='tight')
plt.show()

