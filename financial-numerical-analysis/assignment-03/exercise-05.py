# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_A = np.array([[3, 1, 1], [2, 1, 2], [1, 2, 3]])
arr_B = np.array([[1, 1, -1], [2, -1, 0], [1, -1, 1]])
print(arr_A)
print(arr_B)

#(1) 2A+B
print("2A+B=\n", arr_A*2  + arr_B)

# (2) 4A**2-3B**2
# print(arr_A**2)
# print("4A**2-3B**2=\n", 4*arr_A**2-3*arr_B**2)
#上述算法并没有将A矩阵自己乘自己，而是在对每一个元素做二次方
print("4A**2-3B**2=\n", 4*np.dot(arr_A, arr_A)-3*np.dot(arr_B, arr_B))

#(3) AB
# print(arr_A@arr_B)
print("AB=\n", np.dot(arr_A, arr_B))

#(4) BA
# print(arr_B@arr_A)
print("BA=\n", np.dot(arr_B, arr_A))

#(5) AB-BA
# print(arr_A@arr_B - arr_B@arr_A)
print("AB-BA=\n", np.dot(arr_A, arr_B)-np.dot(arr_B, arr_A))