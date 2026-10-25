# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

# 沪深300在resset上的数据只有2002以后的，故以2002到2019的数据作为分析对象。

data= pd.read_excel('homework12_3_1.xlsx')
data.columns = ['date', 'price']
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
print(data)

# 选出周收盘价
data = data.set_index('date')
print(data)
price_weekly = data['price'].resample('W-Fri').last()
print(price_weekly)

# 计算周收益率
yield_weekly = [0]
for i in range(1, len(price_weekly)):
    rate = (price_weekly.iloc[i]-price_weekly.iloc[i-1])/price_weekly.iloc[i-1]
    yield_weekly.append(rate)
print(yield_weekly)
print(len(yield_weekly))
data_weekly = pd.DataFrame({'price': price_weekly, 'yield': yield_weekly}, index=price_weekly.index)
print(data_weekly)

# 统计频数（与homework7_6有些相似）
bins = np.linspace(-0.12, 0.12, 101)
print(bins)
print(len(bins))
labels = []
for i in range(100):
    labels.append(i+1)
print(labels)
print(len(labels))
# labels一定要比bins少一个
data_weekly['group'] = pd.cut(data_weekly['yield'], bins=bins, labels=labels)
print(data_weekly)
data_weekly_counts = data_weekly.groupby('group', observed=False).size()
# groupby出来的data_weekly_counts是一个series
print(data_weekly_counts)

# 统计频率
freq = []
interval = bins[1] - bins[0]
print(interval)
print(len(data_weekly_counts))
for i in range(len(data_weekly_counts)):
    p = data_weekly_counts.iloc[i]/(interval*len(price_weekly))
    freq.append(p)
print(freq)
data_freq = pd.DataFrame({'amounts': data_weekly_counts, 'freq': freq}, index=data_weekly_counts.index)
print(data_freq)

# 画散点图
r = []
for i in range(1, len(bins)):
    r.append((bins[i-1]+bins[i])/2)
print(r)
plt.figure(1)
plt.scatter(r, data_freq['freq'])

# 极大似然估计计算正态分布的参数
mu = data_weekly['yield'].mean()
sigma = data_weekly['yield'].std()
print("mu=", mu)
print('sigma=', sigma)

# 画图观察正态分布的拟合效果
r_plot = np.linspace(-0.12, 0.12, 100)
p_plot = np.e**(-(r_plot-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma
plt.plot(r_plot, p_plot, '-r')
plt.savefig('homework12_3_scatter.jpg', dpi=300, bbox_inches='tight')
plt.show()
# 收益率数据呈现尖峰肥尾的特性

# 计算数值积分
def integral_fun(x):
    f = np.e**(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma
    return f

def integral_simpson(a, b, n):
    x_0 = a
    x_n = b
    h = (x_n - x_0)/n
    xp = np.arange(x_0, x_n+h, h)
    fxp = integral_fun(xp)
    fxp[1:-1:2] = fxp[1:-1:2]*4
    fxp[2:-1:2] = fxp[2:-1:2]*2
    Sn = np.sum(fxp)*h/3
    return Sn

print("回报率在[-0.12,0.12]内的发生概率为：", integral_simpson(-0.12, 0.12, 512))