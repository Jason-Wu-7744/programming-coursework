# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_A = np.diag([1/3, 1/4, 1/7])
# print(arr_A)
arr_A_minus = np.linalg.inv(arr_A)
# print(arr_A_minus)
# 可以先将BA移到等式左边，同时削去A，再将左边除了B意以外的项全移到右边

arr1 = arr_A_minus - np.eye(3)
# print(arr1)
arr_B = 6*np.linalg.inv(arr1)
print(arr_B)
