# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_B = np.array([[1, 2, -3, -2], [0, 1, 2, -3], [0, 0, 1, 2], [0, 0, 0, 1]])
arr_C = np.array([[1, 2, 0, 1], [0, 1, 2, 0], [0, 0, 1, 2], [0, 0, 0, 1]])
# print(arr_B, "\n", arr_C)

arr_A_transpose = np.linalg.inv(arr_C)@np.linalg.inv((2*np.eye(4)-np.linalg.inv(arr_C)@arr_B))
print(arr_A_transpose.T)
