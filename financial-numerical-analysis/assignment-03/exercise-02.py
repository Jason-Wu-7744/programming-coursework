# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

#创建二维数组
# arr_A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# arr_A = np.arange(1, 17)
# arr_A.shape = 4, 4
arr_A = np.arange(1, 17).reshape(4, 4)
print(arr_A)

#A(1,1)改为0
arr_A[0, 0] = 0
print(arr_A)

#A(2,2)改为A(1,2)和A(2,1)的和
arr_A[1, 1] = arr_A[0, 1] + arr_A[1, 0]
print(arr_A)