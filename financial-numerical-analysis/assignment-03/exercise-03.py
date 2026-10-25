# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(arr_A)

arr_B = np.delete(arr_A, 1, axis = 0)
print(arr_B)

arr_C = np.delete(arr_B, 1, axis = 1)
print(arr_C)
