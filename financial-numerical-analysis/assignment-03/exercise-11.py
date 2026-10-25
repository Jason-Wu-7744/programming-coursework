# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_a = np.array([[2, -3, 0, 2], [1, 5, 2, 1], [3, -1, 1, -1], [4, 1, 2, 2]])
arr_b = np.array([8, 2, 7, 12])
# print(arr_a)

arr_X = np.linalg.solve(arr_a, arr_b)
print(arr_X)