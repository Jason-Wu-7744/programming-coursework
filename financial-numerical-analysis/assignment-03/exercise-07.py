# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

arr_C = np.random.randint(10, 100, size = [20, 20])
# print(arr_C)

for a in range(0, 20):
    for b in range(0, 20):
        if arr_C[a, b] > 80:
            arr_C[a, b] = 110
# print(arr_C)

arr_D = arr_C[2:7]
print(arr_D)