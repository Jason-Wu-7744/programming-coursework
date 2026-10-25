# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

data2015 = pd.read_excel("homework11_2_1.xlsx")
data2015.columns = ['code', 'date', 'yield']
data2015['date'] = pd.to_datetime(data2015['date'], format='%Y-%m-%d')
# print(data2015)

# stock = [568, 25, 543, 600870, 600639, 556, 600694, 600808, 600601, 600630, 600665, 600656, 600610, 540, 600663]
# n_stock = len(stock)
# print(n_stock)
# for i in stock:
#     list_i = []
# 通过写循环的方式来把长表变为宽表实在有些复杂，可以使用pivot方法

data2015 = data2015.pivot(columns='code', index='date', values='yield')
# print(data2015)

#检查是否有缺失值
# print(data2015.isnull().sum())

# data2015 = data2015.fillna(method='ffill')
# data2015 = data2015.fillna(method='bfill')
# 上面两行在使用前补和后补，这对于计算收益率而言很不合理，应当用0来补
data2015 = data2015.fillna(0)
print(data2015.isnull().sum())
print(data2015)
print(data2015.columns)


data2016 = pd.read_excel("homework11_2_2.xlsx")
data2016.columns = ['code', 'date', 'yield']
data2016['date'] = pd.to_datetime(data2016['date'], format='%Y-%m-%d')
# print(data2016)
data2016 = data2016.pivot(index='date', columns='code', values='yield')
# print(data2016)
# print(data2016.isnull().sum())
data2016 = data2016.fillna(0)
print(data2016.isnull().sum())
print(data2016)

# 发现了一个问题，似乎并不存在000556这个股票，故忽略这个股票，只计算14*14的相关系数矩阵

data = pd.concat([data2015, data2016], axis=0)
# axis=0表示纵向拼接
print(data)
print(data.isnull().sum())

data_corr = data.corr()
print('相关系数矩阵为：')
print(data_corr)


def PowerMethod_EigenValueVector(A, E):
    n = len(A)
    # 定义初始特征向量
    z0 = np.random.random((n,1))
    lambda0 = 0.9
    lambda1 = 1.0
    i = 0
    while abs(lambda1 - lambda0) > E:
        lambda0 = lambda1
        w = np.dot(A, z0)
        absw = abs(w)
        # np.argmax返回最大值的索引
        i_maxabsw = np.argmax(absw)
        # 标准化特征向量和特征值
        z1 = w/w[i_maxabsw]
        lambda1 = w[0]/z0[0]
        # 一旦选定了k=0，就不能再发生改变
        print("第"+str(i)+"次迭代的特征值为：")
        print(lambda1[0])
        print("第"+str(i)+"次迭代的特征向量为：")
        print(z0)
        i += 1
        z0 = z1
    eigvalue = lambda1
    eigvector = z1
    return eigvalue, eigvector

eigvalue, eigvector = PowerMethod_EigenValueVector(data_corr, 10**-6)
print("特征值为：\n", eigvalue[0])
print("特征向量为：\n", eigvector)