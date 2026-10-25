# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
arr = np.array(pd.read_excel("exercise-18_1.xlsx"))
print(arr)
time = arr[:, 0]
print(time)
arr = np.delete(arr, 0, 1)
# print(arr.dtype)
#可以发现读入数据时一旦包含字符串，后续即使去掉了字符串其他数据仍然不是浮点型，要用astype改变数据类型
arr = arr.astype(float)
print(arr)

# arr190617 = arr[0, :]
# print(arr190617.shape)
# arr190617.T
#一维数组转置无效，需要变为二维数组才行
arr190617 = arr[0, :].reshape(-1,  1)
# print(arr190617.shape)
arr190618 = arr[1, :].reshape(-1,  1)
arr190619 = arr[2, :].reshape(-1,  1)
arr190620 = arr[3, :].reshape(-1,  1)
arr190621 = arr[4, :].reshape(-1,  1)
arr190624 = arr[5, :].reshape(-1,  1)
arr190625 = arr[6, :].reshape(-1,  1)
arr190626 = arr[7, :].reshape(-1,  1)
arr190627 = arr[8, :].reshape(-1,  1)
arr190628 = arr[9, :].reshape(-1,  1)

arr_transposed = np.hstack((arr190617, arr190618, arr190619, arr190620, arr190621, arr190624, arr190625, arr190626, arr190627, arr190628))
print(arr_transposed, arr_transposed.shape)
# arr_transposed = np.concatenate((arr190617, arr190618, arr190619, arr190620, arr190621, arr190624, arr190625, arr190626, arr190627, arr190628), 1)
# print(arr_transposed, arr_transposed.shape)

#第二小题
print(arr_transposed)
arr_cov = np.cov(arr_transposed)
arr_corrcoef = np.corrcoef(arr_transposed)
print("不同指数之间的协方差矩阵为：\n", arr_cov)
print("不同指数之间的关系数矩阵为：\n", arr_corrcoef)

#第三小题
arr_cov_diag = np.diag(arr_cov)
print("协方差矩阵的对角线:", arr_cov_diag)
arr_cov_triu = np.triu(arr_cov)
print("协方差矩阵的上三角部分:", arr_cov_triu)
arr_cov_tril = np.tril(arr_cov)
print("协方差矩阵的下三角部分:", arr_cov_tril)
arr_cov_trace = np.trace(arr_cov)
print("协方差矩阵的迹:", arr_cov_trace)

#第三小题
arr_cov_diag = np.diag(arr_cov)
print("协方差矩阵的对角线:", arr_cov_diag)
arr_cov_triu = np.triu(arr_cov)
print("协方差矩阵的上三角部分:", arr_cov_triu)
arr_cov_tril = np.tril(arr_cov)
print("协方差矩阵的下三角部分:", arr_cov_tril)
arr_cov_trace = np.trace(arr_cov)
print("协方差矩阵的迹:", arr_cov_trace)

#第四小题
arr_corrcoef_diag = np.diag(arr_corrcoef)
print("相关系数矩阵的对角线:", arr_corrcoef_diag)
arr_corrcoef_triu = np.triu(arr_corrcoef)
print("相关系数矩阵的上三角部分:", arr_corrcoef_triu)
arr_corrcoef_tril = np.tril(arr_corrcoef)
print("相关系数矩阵的下三角部分:", arr_corrcoef_tril)
arr_corrcoef_trace = np.trace(arr_corrcoef)
print("相关系数矩阵的迹:", arr_corrcoef_trace)