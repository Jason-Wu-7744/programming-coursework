# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
arr = np.array(pd.read_excel("exercise-19_1.xlsx"))
print(arr)
name = arr[:, 0]
print(name)
arr = np.delete(arr, 0, 1)
arr = arr.astype(float)
print(arr.dtype)
arr_weight = arr[:, -1]
print("每只股票投资权重的数组:\n", arr_weight)
tuple_value = {}
for i in range(0, 5):
    tuple_value[name[i]] = 30000000*arr_weight[i]
# print(tuple_value)
arr_rate = np.delete(arr, -1, 1)
print("股票涨跌幅的数组:\n", arr_rate)
date = ["2019/7/29", "2019/7/30", "2019/7/31", "2019/8/1", "2019/8/2"]
all_reward = 0
for a in range(0, 5):
    date_reward = 0
    for b in range(0, 5):
        date_reward += tuple_value[name[b]]*arr_rate[b, a]
    print(date[a], "的日盈亏金额为", date_reward, "元")
    all_reward += date_reward
print("累积盈亏金额为",  all_reward, "元")

#第二小题
arr_rate_det = np.linalg.det(arr_rate)
print("股票价格涨跌幅矩阵的行列式：\n", arr_rate_det)
arr_rate_inv = np.linalg.inv(arr_rate)
print("股票价格涨跌幅矩阵的逆：\n", arr_rate_inv)

arr_rate_eig = np.linalg.eig(arr_rate)
print("股票价格涨跌幅矩阵的特征值分解：\n", arr_rate_eig)
arr_rate_svd = np.linalg.svd(arr_rate)
print("股票价格涨跌幅矩阵的奇异值分解：\n", arr_rate_svd)

#第三小题
arr_rate_corrcoef = np.corrcoef(arr_rate)
print("股票票价格涨跌幅的相关系数矩阵:\n", arr_rate_corrcoef)

arr_rate_corrcoef_qr = np.linalg.qr(arr_rate_corrcoef)
print("该矩阵的正交三角（QR）分解:\n", arr_rate_corrcoef_qr)

# arr_rate_corrcoef_cholesky = np.linalg.cholesky(arr_rate_corrcoef)
# print("该矩阵的乔斯基分解:\n", arr_rate_corrcoef_cholesky)
#只有正定矩阵才可以做乔斯基分解

print("股票票价格涨跌幅的相关系数矩阵无法做乔斯基分解")
