# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

A = np.array([[2, 1, -1, 2], [4, 4, 1, 3], [-6, -1, 10, 10], [-2, 1, 8, 4]])
b = np.array([[2], [4], [-5], [1]])

# 定义LU分解函数
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
    n = len(A[:, 0])
    g = np.dot(np.linalg.inv(L), b)
    x = np.zeros([n, 1])
    x[n - 1] = g[n - 1] / U[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (g[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    root = x
    return root

print("求根结果为：\n", backinteratioin_LU(A, b))
