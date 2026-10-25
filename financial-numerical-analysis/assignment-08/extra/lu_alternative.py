# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import numpy as np

def lu_decomposition(A):
    """
    对矩阵 A 进行 LU 分解（Doolittle 方法）
    返回 L 和 U，满足 A = LU，L 为单位下三角矩阵，U 为上三角矩阵
    """
    n = A.shape[0]
    L = np.eye(n)  # 单位矩阵
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        # 计算 U 的第 i 行
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # 计算 L 的第 i 列
        for j in range(i + 1, n):
            if U[i, i] == 0:
                raise ValueError("LU 分解失败：主对角线元素为 0")
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U

A = np.array([[2, 1, -1, 2], [4, 4, 1, 3], [-6, -1, 10, 10], [-2, 1, 8, 4]])
print(lu_decomposition(A))