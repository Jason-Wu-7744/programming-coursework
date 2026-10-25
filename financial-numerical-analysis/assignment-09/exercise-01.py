# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

A = np.array([[3, -1, 1],
              [1, 3, 1],
              [1, 2, 7]])
b = np.array([[7],
              [-3],
              [11]])

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
            print(x1)
    return x1
print('根为：\n', jacobi_iteration(A, b, 0.1))
