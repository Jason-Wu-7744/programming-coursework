# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

def jacobi_iteration(A, b, e):
    n = len(A[:, 0])
    x0 = np.zeros([n, 1])
    x1 = np.zeros([n, 1])
    for i in range(n):
        sum_bonus = 0
        for a in range(n):
            if i != a:
                sum_bonus += A[i, a]*x0[a]
        x1[i] = 1/A[i, i]*(b[i]-sum_bonus)
    while np.abs(np.abs(x1).sum()-np.abs(x0).sum()) > e:
        x0 = x1.copy()
        # .copy至关重要，把x1存为副本，x1和x2分开。改变x1不会影响x2.
        for i in range(n):
            sum_bonus = 0
            for a in range(n):
                if i != a:
                    sum_bonus += A[i, a] * x0[a]
            x1[i] = 1 / A[i, i] * (b[i] - sum_bonus)
            # print(x1)
    return x1

def GaussSeidel_iteration(A, b, e):
    n = len(A[:, 0])
    x0 = np.zeros([n, 1])
    x1 = np.zeros([n, 1])
    for i in range(n):
        sum_bonus = 0
        for a in range(n):
            if i != a:
                sum_bonus += A[i, a]*x1[a]  #区别
        x1[i] = 1/A[i, i]*(b[i]-sum_bonus)
    while np.abs(np.abs(x1).sum()-np.abs(x0).sum()) > e:
        x0 = x1.copy()
        # .copy至关重要，把x1存为副本，x1和x2分开。改变x1不会影响x2.
        for i in range(n):
            sum_bonus = 0
            for a in range(n):
                if i != a:
                    sum_bonus += A[i, a] * x1[a]  #区别
            x1[i] = 1 / A[i, i] * (b[i] - sum_bonus)
            # print(x1)
    return x0

# 使用总市值加权因子SMB、HML
data_x = pd.read_excel('2015_2024_三因子.xlsx')
data_x.columns = ['date', 'RMRF', 'SMB', 'HML']
data_y1 = pd.read_excel('2015_2024_上证医药.xlsx')
data_y1.columns = ['date', 'med']
data_y2 = pd.read_excel('2015_2024_上证能源.xlsx')
data_y2.columns = ['date', 'eng']
data_y3 = pd.read_excel('2015_2024_上证材料.xlsx')
data_y3.columns = ['date', 'mat']

data = pd.concat([data_x, data_y1, data_y2, data_y3], axis=1)
print(data.columns)
data = data.drop(columns='date')
print(data.columns)
print(data)

x1 = data['RMRF']
x2 = data['SMB']
x3 = data['HML']
sum_x1 = x1.sum()
sum_x2 = x2.sum()
sum_x3 = x3.sum()

output_name = ['上证医药', '上证能源', '上证材料']
output = ['med', 'eng', 'mat']
for a in range(3):
    y = data[output[a]]
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
    n = len(x1)
    for i in range(n):
        sum_x1x1 += x1[i] ** 2
        sum_x2x2 += x2[i] ** 2
        sum_x3x3 += x3[i] ** 2
        sum_yx1 += y[i] * x1[i]
        sum_yx2 += y[i] * x2[i]
        sum_yx3 += y[i] * x3[i]
        sum_x1x2 += x1[i] * x2[i]
        sum_x1x3 += x1[i] * x3[i]
        sum_x2x3 += x2[i] * x3[i]
    A = np.array([[n, sum_x1, sum_x2, sum_x3],
                  [sum_x1, sum_x1x1, sum_x1x2, sum_x1x3],
                  [sum_x2, sum_x1x2, sum_x2x2, sum_x2x3],
                  [sum_x3, sum_x1x3, sum_x2x3, sum_x3x3]])
    b = np.array([[sum_y],
                  [sum_yx1],
                  [sum_yx2],
                  [sum_yx3]])
    print(output_name[a], "用雅可比迭代法的计算结果：")
    print(jacobi_iteration(A, b, 0.01))
    print(output_name[a], "用高斯—赛德尔迭代法的计算结果：")
    print(GaussSeidel_iteration(A, b, 0.01))

# 回归的A，b公式要记忆准确
