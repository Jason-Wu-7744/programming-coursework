# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data_q = pd.read_excel("homework13_1_1.xlsx")
print(data_q)

# 向前差分
data_front = data_q

# alpha = []
# for i in range(0, len(data_q['q'])-1):
#     alpha.append((data_q['τ(q)'][i+1]-data_q['τ(q)'][i])/(data_q['q'][i+1]-data_q['q'][i]))
# print(alpha)
# print(len(alpha))
data_front['alpha'] = np.nan
for i in range(0, len(data_q['q'])-1):
    data_front['alpha'][i] = (data_q['τ(q)'][i+1]-data_q['τ(q)'][i])/(data_q['q'][i+1]-data_q['q'][i])
# print(data_front)

data_front['f(alpha)'] = data_front['q']*data_front['alpha'] - data_front['τ(q)']
print("向前差分：")
print(data_front)

plt.figure(1)
# plt.plot(data_front['q'], data_front['τ(q)'])
plt.plot(data_front['alpha'], data_front['f(alpha)'], 'd-b')


# 向后差分
data_back = data_q
data_back['alpha'] = np.nan
for i in range(1, len(data_q['q'])):
    data_back['alpha'][i] = (data_q['τ(q)'][i]-data_q['τ(q)'][i-1])/(data_q['q'][i]-data_q['q'][i-1])
# print(data_back)

data_back['f(alpha)'] = data_back['q']*data_back['alpha'] - data_back['τ(q)']
print("向后差分：")
print(data_back)

plt.plot(data_back['alpha'], data_back['f(alpha)'], 'o-r')


# 中心差分
data_center = data_q
data_center['alpha'] = np.nan
for i in range(1, len(data_q['q'])-1):
    data_center['alpha'][i] = (data_q['τ(q)'][i+1]-data_q['τ(q)'][i-1])/(data_q['q'][i+1]-data_q['q'][i-1])
# print(data_center)

data_center['f(alpha)'] = data_center['q']*data_center['alpha'] - data_center['τ(q)']
print("中心差分：")
print(data_center)

plt.plot(data_center['alpha'], data_center['f(alpha)'], 's-k')
plt.legend(['front_diff', 'back_diff', 'center_diff'])
plt.savefig('homework13_1.jpg', dpi=300, bbox_inches='tight')

plt.show()


# 上述写法可能存在链式赋值的问题，写为
# data_front.loc['i', 'alpha']或许更为合适