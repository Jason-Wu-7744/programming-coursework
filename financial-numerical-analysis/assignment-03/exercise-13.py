# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

#第一小题
arr_AMAZON = np.array([1822.68, 1840.12, 1871.15, 1907.57, 1869.00])
list_APPLE = [185.72, 188.66, 190.92, 190.08, 189.00]
arr_APPLE = np.array(list_APPLE)
print(arr_AMAZON, "\n", arr_APPLE )

#第二小题
arr = np.array([[1822.68, 1840.12, 1871.15, 1907.57, 1869.00], [185.72, 188.66, 190.92, 190.08, 189.00], [123.35, 124.73, 126.02, 128.93, 128.07], [1136.59, 1124.86, 1170.80, 1184.50, 1168.78], [345.26, 345.61, 354.99, 359.31, 354.45]])
print(arr, "\n", arr.shape, "\n", arr.ndim, "\n", arr.size, "\n", arr.dtype)

#第三小题
arr1 = np.array(np.arange(0, arr.size+1))
# print(arr1)
arr2 = np.array(np.linspace(arr[1, 0], arr[1, 4], 40))
# print(arr2)

#第四小题
arr3 = np.zeros((1, 5))
arr4 = np.zeros((5, 5))
arr5 = np.ones((1, 5))
arr6 = np.ones((5, 5))
print(arr3, "\n", arr4, "\n", arr5, "\n", arr6)