# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

def jacobi_iteration(A, b, e, max_iter=10000):
    """Course iteration with an iterate-difference/residual stop and finite cap."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).reshape(-1, 1)
    n = len(b)
    if A.shape != (n, n) or not np.all(np.isfinite(A)) or not np.all(np.isfinite(b)):
        raise ValueError("A and b must be finite and have compatible dimensions")
    if e <= 0 or not np.isfinite(e) or max_iter < 1 or np.any(np.diag(A) == 0):
        raise ValueError("Require positive tolerance/iteration limit and nonzero diagonal")
    x = np.zeros((n, 1))
    for iteration in range(max_iter):
        old = x.copy()
        for i in range(n):
            total = sum(A[i, j] * old[j, 0] for j in range(n) if j != i)
            x[i, 0] = (b[i, 0] - total) / A[i, i]
        if not np.all(np.isfinite(x)):
            raise RuntimeError("Jacobi iteration diverged")
        if np.linalg.norm(x - old, np.inf) <= e and np.linalg.norm(A @ x - b, np.inf) <= e:
            return x
    raise RuntimeError("Jacobi did not converge within max_iter")

def GaussSeidel_iteration(A, b, e, max_iter=10000):
    """Course iteration with an iterate-difference/residual stop and finite cap."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).reshape(-1, 1)
    n = len(b)
    if A.shape != (n, n) or not np.all(np.isfinite(A)) or not np.all(np.isfinite(b)):
        raise ValueError("A and b must be finite and have compatible dimensions")
    if e <= 0 or not np.isfinite(e) or max_iter < 1 or np.any(np.diag(A) == 0):
        raise ValueError("Require positive tolerance/iteration limit and nonzero diagonal")
    x = np.zeros((n, 1))
    for iteration in range(max_iter):
        old = x.copy()
        for i in range(n):
            total = sum(A[i, j] * x[j, 0] for j in range(n) if j != i)
            x[i, 0] = (b[i, 0] - total) / A[i, i]
        if not np.all(np.isfinite(x)):
            raise RuntimeError("Gauss-Seidel iteration diverged")
        if np.linalg.norm(x - old, np.inf) <= e and np.linalg.norm(A @ x - b, np.inf) <= e:
            return x
    raise RuntimeError("Gauss-Seidel did not converge within max_iter")

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
