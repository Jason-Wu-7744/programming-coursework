# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
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


# 第一幅图（正态分布拟合）：
# 显然，用回归并不适合拟合正态分布，用极大似然估计比较合适
mu = data['r'].mean()
sigma = data['r'].std()

x_show = np.linspace(-0.0052, 0.0052, 10000)
# 一开始画出的正态分布过于巨大，通过缩小x的范围实现了例图的样式
y_show = np.e**(-(x_show-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
plt.figure(1)
plt.semilogy(x_show, y_show, '-b', lw=1.5)

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
delta = bins[1] - bins[0]
for i in range(len(group_counts['group'])):
    p = group_counts.iloc[i, 0]/delta/len(data['r'])
    freq.append(p)
print(freq)
print(len(freq))

bins_x_axis = []
for i in range(1, len(bins)):
    x_axis = (bins[i]+bins[i-1])/2
    bins_x_axis.append(x_axis)

group_counts['r'] = bins_x_axis
group_counts['p'] = freq

plt.scatter(group_counts['r'], group_counts['p'], s=6, marker='s', c='red')
plt.yticks(np.logspace(-4, 4, 5))
plt.xlabel(r'$r$', fontsize=25, fontname='times new roman')
plt.ylabel(r'$p(r)$', fontsize=25, fontname='times new roman')
plt.xticks(np.linspace(-0.1, 0.1, 5), fontsize=20, fontname='times new roman')
plt.yticks(np.logspace(-4, 4, 5), fontsize=20, fontname='times new roman')
plt.legend(['normal fit', 'PDF-return-tick'], loc='upper left', fontsize=15)
# legend中似乎没有办法调整字体，不识别fontname， 调节字体的方法有待后续的学习
plt.savefig('exercise-06_1.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-06_1.jpg', dpi=300, bbox_inches='tight')
plt.show()


# 第二幅图：（取对线性回归）
data = data.drop(columns='group')

# 注意到例图中的r的正负区间是分别回归的，这很合理，因为r为负时需要取绝对值再取对
dfs = {name: g.reset_index(drop=True)
       for name, g in data.groupby(np.sign(data['r']))}
data_pos, data_neg, data_zero = dfs[1], dfs[-1], dfs[0]

print(data_pos)
print(data_neg)
print(data_zero)

#开始计算data_pos的概率密度
bins = np.logspace(-3, -1, 22)
print(len(bins))
labels = []
for i in range(21):
    labels.append(i+1)
print(labels)
data_pos['group'] = pd.cut(data_pos['r'], bins=bins, labels=labels)
print(data_pos)
group_counts_pos = data_pos.groupby('group', observed=False).size()
print(group_counts_pos)
group_counts_pos = pd.DataFrame(group_counts_pos, columns=['group'])
print(group_counts_pos)
#算r，p以便回归和画图
freq = []
for i in range(len(group_counts_pos['group'])):
    p = group_counts_pos.iloc[i, 0]/(bins[i+1]-bins[i])/len(data_pos['r'])
    freq.append(p)
print(freq)
print(len(freq))
bins_x_axis = []
for i in range(1, len(bins)):
    x_axis = (bins[i]+bins[i-1])/2
    bins_x_axis.append(x_axis)
group_counts_pos['r'] = bins_x_axis
group_counts_pos['p'] = freq
print(group_counts_pos)
plt.figure(2)
plt.scatter(group_counts_pos['r'], group_counts_pos['p'], s=8, c='none', edgecolors='r', marker='o', label='pos tail')
plt.xscale('log')
plt.yscale('log')
plt.xticks(np.logspace(-3, -1, 3))
plt.yticks(np.logspace(-6, 4, 6))
# plt.show()
# 开始回归pos
n = len(group_counts_pos['r'])
sum_x = np.log(group_counts_pos['r']).sum()
sum_y = np.log(group_counts_pos['p']).sum()
sum_xx = 0
for i in range(n):
    sum_xx += np.log(group_counts_pos.iloc[i, 1])**2
sum_xy = 0
for i in range(n):
    sum_xy += np.log(group_counts_pos.iloc[i, 1])*np.log(group_counts_pos.iloc[i, 2])
A = np.array([[n, sum_x],
              [sum_x, sum_xx]
              ])
b = np.array([[sum_y],
              [sum_xy]
              ])
x = np.dot(np.linalg.inv(A), b)
print(x)
x_show = np.logspace(-3, -1, 100)
y_show = x_show**x[1, 0]*np.e**x[0, 0]
plt.loglog(x_show, y_show, '-r', lw=1.5)


#开始计算data_neg的概率密度
data_neg['r'] = np.abs(data_neg['r'] )
bins = np.logspace(-3, -1, 22)
print(len(bins))
labels = []
for i in range(21):
    labels.append(i+1)
print(labels)
data_neg['group'] = pd.cut(data_neg['r'], bins=bins, labels=labels)
print(data_pos)
group_counts_neg = data_neg.groupby('group', observed=False).size()
print(group_counts_neg)
group_counts_neg = pd.DataFrame(group_counts_neg, columns=['group'])
print(group_counts_neg)
#算r，p以便回归和画图
freq = []
for i in range(len(group_counts_neg['group'])):
    p = group_counts_neg.iloc[i, 0]/(bins[i+1]-bins[i])/len(data_neg['r'])
    freq.append(p)
print(freq)
print(len(freq))
bins_x_axis = []
for i in range(1, len(bins)):
    x_axis = (bins[i]+bins[i-1])/2
    bins_x_axis.append(x_axis)
group_counts_neg['r'] = bins_x_axis
group_counts_neg['p'] = freq
print(group_counts_neg)
plt.scatter(group_counts_neg['r'], group_counts_neg['p'], s=8, c='none', edgecolors='b', marker='s', label='neg tail')
plt.xscale('log')
plt.yscale('log')
plt.xticks(np.logspace(-3, -1, 3))
plt.yticks(np.logspace(-6, 4, 6))
# 开始回归neg
n = len(group_counts_neg['r'])
sum_x = np.log(group_counts_neg['r']).sum()
sum_y = np.log(group_counts_neg['p']).sum()
sum_xx = 0
for i in range(n):
    sum_xx += np.log(group_counts_neg.iloc[i, 1])**2
sum_xy = 0
for i in range(n):
    sum_xy += np.log(group_counts_neg.iloc[i, 1])*np.log(group_counts_neg.iloc[i, 2])
A = np.array([[n, sum_x],
              [sum_x, sum_xx]
              ])
b = np.array([[sum_y],
              [sum_xy]
              ])
x = np.dot(np.linalg.inv(A), b)
print(x)
x_show = np.logspace(-3, -1, 100)
y_show = x_show**x[1, 0]*np.e**x[0, 0]
plt.loglog(x_show, y_show, '-b', lw=1.5)

plt.xlabel(r'$r$', fontsize=25, fontname='times new roman')
plt.ylabel(r'$p(r)$', fontsize=25, fontname='times new roman')
plt.xticks(np.logspace(-3, -1, 3), fontsize=20, fontname='times new roman')
plt.yticks(np.logspace(-6, 4, 6), fontsize=20, fontname='times new roman')
plt.legend(loc='upper right', fontsize=17)
plt.text(10**(-2), 10**0.5, r'$-(α_{neg}+1)=-3.676$', fontsize=20)
plt.text(10**(-3), 10**(-4), r'$-(α_{pos}+1)=-3.837$', fontsize=20)
#text 似乎也没有办法用fontname设置字体
plt.savefig('exercise-06_2.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-06_2.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 计算结果与图片展示效果与例图有些许差别，算法优化有待后续的学习
