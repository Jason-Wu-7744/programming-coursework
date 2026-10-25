# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_A = np.array([[2, -1], [-1, 2]])
arr_B = np.array([[0, -2], [-2, 0]])

arr_X = (2*arr_A + arr_B)/2
print(arr_X)