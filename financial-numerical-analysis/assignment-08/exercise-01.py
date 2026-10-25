# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

# 选主元
# 返回（k, k）之后的换好主元的矩阵，确保第一行第一列的元素最大，从而乘数变小，误差最小
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
def LinearEquation_GEPivot(A, b):
    root = Equation_GEPivot(A, b)
    print("根为：\n", root)
    return root

A = np.array([[2, 1, -1, 2], [4, 4, 1, 3], [-6, -1, 10, 10], [-2, 1, 8, 4]])
b = np.array([[2], [4], [-5], [1]])
print(LinearEquation_GEPivot(A, b))