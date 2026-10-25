# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr1 = np.random.randn(100, 100)
# print(arr1, "/n", arr1.shape)
# print(arr1[9, :])

a = 0
for i in arr1[9, :]:
    if i < 0:
        arr1[9, a] = -0.5
    a += 1
# print(arr1[9, :])

a = 0
for i in arr1[54, :]:
    if i < 0:
        arr1[54, a] = -0.5
    a += 1
# print(arr1[54, :])

a = 0
for i in arr1[:, 17]:
    if i < 0:
        arr1[a, 17] = -0.5
    a += 1
# print(arr1[:, 17])

a = 0
for i in arr1[:, 76]:
    if i < 0:
        arr1[a, 76] = -0.5
    a += 1
# print(arr1[:, 76])

arr2 = np.delete(arr1, (24, 57, ), 0)
# print(arr2.shape)
arr2 = np.delete(arr2, (37, 73), 1)
print(arr2.shape, "\n", arr2)
