# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(arr_A)

arr_B = arr_A[1:3, 1:3]
# arr_B = arr_A[1:3, (1, 2)]
# arr_B = arr_A[(1, 2), 1:3]
print(arr_B)

arr_C = np.delete(arr_A, (1, 2), 1)
# print(arr_C)
arr_C = np.delete(arr_C, (1, 2), 0)
print(arr_C)

# arr_C = arr_A[(0, 0, 3, 3), (0, 3, 0, 3)]
# print(arr_C)
#通过索引的方式来取这些值只会得到一个一维数组


