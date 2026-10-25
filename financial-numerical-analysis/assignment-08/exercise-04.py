# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data = pd.read_csv('Exp08-Python-实验数据-LPPLS模型估参.csv', encoding='GB2312')
data.columns = ['time', 'close']
data['time'] = pd.to_datetime(data['time'], format=' %Y/%m/%d')
print(data)

n = len(data['time'])

t = []
tc = (pd.to_datetime('2016/10/25', format='%Y/%m/%d')-pd.to_datetime('2016/01/01', format='%Y/%m/%d'))/np.timedelta64(1, 'D')
print(tc)
for i in range(n):
    time_revised = (data['time'][i]-pd.to_datetime('2016/01/01', format='%Y/%m/%d'))/np.timedelta64(1, 'D')
    print(time_revised)
    time_revised = tc - time_revised
    t.append(time_revised)
data['tc_t'] = t
print(data)
data['ln_tc_t'] = np.log(data['tc_t'])
m = 0.2932
data['B'] = data['tc_t']**m
w = 6.1023
data['C1'] = data["tc_t"]**m*np.cos(w*np.log(data['tc_t']))
data['C2'] = data["tc_t"]**m*np.sin(w*np.log(data['tc_t']))
data['ln_p'] = np.log(data['close'])
print(data)

x1 = data['B']
x2 = data['C1']
x3 = data['C2']
y = data['ln_p']

sum_x1 = x1.sum()
sum_x2 = x2.sum()
sum_x3 = x3.sum()
sum_y = y.sum()

sum_x1x1 = 0
sum_x2x2 = 0
sum_x3x3 = 0
sum_yx1 = 0
sum_yx2 = 0
sum_yx3 = 0
sum_x1x2 = 0
sum_x1x3 = 0
sum_x2x3 = 0
for i in range(n):
    sum_x1x1 += data['B'][i]**2
    sum_x2x2 += data['C1'][i]**2
    sum_x3x3 += data['C2'][i]**2
    sum_yx1 += y[i]*x1[i]
    sum_yx2 += y[i]*x2[i]
    sum_yx3 += y[i]*x3[i]
    sum_x1x2 += x1[i]*x2[i]
    sum_x1x3 += x1[i]*x3[i]
    sum_x2x3 += x2[i]*x3[i]

A = np.array([[n, sum_x1, sum_x2, sum_x3],
              [sum_x1, sum_x1x1, sum_x1x2, sum_x1x3],
              [sum_x2, sum_x1x2, sum_x2x2, sum_x2x3],
              [sum_x3, sum_x1x3, sum_x2x3, sum_x3x3]])
b = np.array([[sum_y],
              [sum_yx1],
              [sum_yx2],
              [sum_yx3]])

print(A, b)

x = np.dot(np.linalg.inv(A), b)
print(x)

plt.figure(1)
plt.scatter(data['time'], data['ln_p'])

x_show = pd.date_range('2016-01-04', '2016-10-18', freq='D')
x_show_t = (x_show - pd.to_datetime('2016/01/01', format='%Y/%m/%d'))/np.timedelta64(1, 'D')
x_show_tc_t = tc - x_show_t
x_show_t_m = x_show_tc_t**m
y_show = x[0, 0] + x[1, 0]*x_show_t_m + x[2, 0]*x_show_t_m*np.cos(w*np.log(x_show_t)) + x[3, 0]*x_show_t_m*np.sin(w*np.log(x_show_t))
plt.plot(x_show, y_show, '-r')
plt.legend(['real value', 'fitted value'])
plt.xticks(pd.to_datetime(['2016/01/01', '2016/06/01', '2016/10/25'], format='%Y/%m/%d'))
plt.xlabel(r"$t$")
plt.ylabel(r"$lnp(t)$")
plt.savefig('exercise-04.jpg', dpi=600, bbox_inches='tight')
plt.show()
