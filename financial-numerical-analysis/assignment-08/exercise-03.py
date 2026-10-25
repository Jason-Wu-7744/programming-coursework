# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

data = pd.read_csv('Exp08-Python-实验数据-因子模型估参.csv', encoding='GB2312')
data.columns = ['Date', 'rm', 'port1', 'port2', 'port3', 'port4', 'port5', 'rf', 'SMB', 'HML']

# concat中axis=o是纵向拼接, 拼接一列组成的列表

port_col = ['port1', 'port2', 'port3', 'port4', 'port5']
port_long = pd.concat([data[col] for col in port_col], axis=0).reset_index(drop=True)
port_long.name = 'port'

others_col = ['Date', 'rm', 'rf', 'SMB', 'HML']
others_long = pd.concat([data[others_col]]*5, axis=0).reset_index(drop=True)

data = pd.concat([port_long, others_long], axis=1)
print(data)


n = len(data['port'])
data['rm_rf'] = data['rm'] - data['rf']
data['ri_rf'] = data['port'] - data['rf']
print(data)

x1 = data['rm_rf']
x2 = data['SMB']
x3 = data['HML']
y = data['ri_rf']

sum_x1 = data['rm_rf'].sum()
sum_x2 = data['SMB'].sum()
sum_x3 = data['HML'].sum()
sum_y = data['ri_rf'].sum()

sum_x1x1 = 0
sum_x2x2 = 0
sum_x3x3 = 0
for i in data['rm_rf']:
    sum_x1x1 += i**2
for i in data['SMB']:
    sum_x2x2 += i**2
for i in data['HML']:
    sum_x3x3 += i**2

sum_yx1 = 0
sum_yx2 = 0
sum_yx3 = 0
sum_x1x2 = 0
sum_x1x3 = 0
sum_x2x3 = 0
for i in range(n):
    sum_yx1 += data['ri_rf'][i]*data['rm_rf'][i]
    sum_yx2 += data['ri_rf'][i]*data['SMB'][i]
    sum_yx3 += data['ri_rf'][i]*data['HML'][i]
    sum_x1x2 += data['rm_rf'][i]*data['SMB'][i]
    sum_x1x3 += data['rm_rf'][i]*data['HML'][i]
    sum_x2x3 += data['SMB'][i]*data['HML'][i]

A = np.array([[n, sum_x1, sum_x2, sum_x3],
              [sum_x1, sum_x1x1, sum_x1x2, sum_x1x3],
              [sum_x2, sum_x1x2, sum_x2x2, sum_x2x3],
              [sum_x3, sum_x1x3, sum_x2x3, sum_x3x3]])
b = np.array([[sum_y],
              [sum_yx1],
              [sum_yx2],
              [sum_yx3]])

print(A, b)


# 高斯消元法解线性方程组
def choose_pivot(Au, k):
    B = Au[k:, k:]
    imb = np.argmax(np.abs(B[:, 0]))
    if imb!=0:
        B1 = B[0, :].copy()
        B[0, :] = B[imb, :]
        B[imb, :] = B1
    Au[k:, k:] = B
    return Au
# 高斯消元
def GussianElemination(Au, k):
    # 最大的第一个元的一行为rowk
    rowk = Au[k, :]
    # k以下的部分矩阵
    matrix_underk = Au[k+1:, :]
    for i in range(len(matrix_underk[:, 0])):
        mk = matrix_underk[i, k]/rowk[k]
        matrix_underk[i, :] = matrix_underk[i, :] - mk*rowk
    Au[k+1:, :] = matrix_underk
    return Au
# 回代求根
def BackInteration(U, g, n):
    x = np.zeros([n, 1])
    # 最后一个x可以直接算出
    x[n - 1] = g[n - 1] / U[n - 1, n - 1]
    # 从倒数第二个x开始往回算，先减去之前算出的x和u对应项的乘积。
    for i in range(n - 2, -1, -1):
        x[i] = (g[i] - np.dot(U[i, i + 1:], x[i + 1:]))/U[i, i]
    root = x
    return root
# 求根程序
def Equation_GEPivot(A, b):
    Au = np.concatenate((A, b), axis=1)
    n = len(Au[:, 0])
    k = 0
    while k < n:
        # 选主元
        Au = choose_pivot(Au, k)
        # 高斯消元
        Au = GussianElemination(Au, k)
        k = k + 1
    # 回代求根
    U = Au[:, 0:n]
    g = Au[:, n]
    root = BackInteration(U, g, n)
    print("上三角矩阵为：\n", U)
    return root
# 主程序
def LinearEquation_GEPivot():
    A = np.array([[n, sum_x1, sum_x2, sum_x3],
                  [sum_x1, sum_x1x1, sum_x1x2, sum_x1x3],
                  [sum_x2, sum_x1x2, sum_x2x2, sum_x2x3],
                  [sum_x3, sum_x1x3, sum_x2x3, sum_x3x3]])
    b = np.array([[sum_y],
                  [sum_yx1],
                  [sum_yx2],
                  [sum_yx3]])
    root = Equation_GEPivot(A, b)
    print("根为：\n", root)
    # return root
print(LinearEquation_GEPivot())


# LU分解法
def SolveEqs_LU(A):
    n = len(A[:, 0])
    L = np.eye(n)
    U = np.zeros([n, n])
    for k in range(n):
        for j in range(k, n):
            sum_U = 0
            for s in range(k):
                sum_U += L[k, s]*U[s, j]
            U[k, j] = A[k, j]-sum_U
            # print(U[k, j])

        for i in range(k + 1, n):
            sum_L = 0
            for s in range(k):
                sum_L += L[i, s] * U[s, k]
            L[i, k] = (A[i, k] - sum_L)/U[k, k]
    return U, L

print("U和L分别为：\n", SolveEqs_LU(A))
# 可以发现高斯消元法和LU分解法求出的U并不相同
# 定义用LU分解的U求根的函数
def backinteratioin_LU(A, b):
    U, L = SolveEqs_LU(A)
    g = np.dot(np.linalg.inv(L), b)
    x = np.dot(np.linalg.inv(U), g)
    return x

print("求根结果为：\n", backinteratioin_LU(A, b))

x = np.dot(np.linalg.inv(A), b)
print(x)
print("α=", x[0, 0])
print('β=', x[1, 0])
print('s=', x[2, 0])
print('h=', x[3, 0])
#可以发现高斯消元法、LU分解法、矩阵乘法三者算出的结果相差不大
