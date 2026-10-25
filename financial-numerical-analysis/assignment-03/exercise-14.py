# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
arr = pd.read_excel("exercise-14_1.xlsx", header=0)
arr = np.delete(arr, (0, 1), 1)
print(arr)
print("阿里健康在2019年2月的涨跌幅为", arr[0, 1], "\n", "腾讯控股在2019年3月的涨跌幅为", arr[2, 2], "\n", "美团点评在2019年6月的涨跌幅为", arr[4, 5])

#第二小题
uplist = []
downlist = []
for a in range(arr.shape[0]):
    for b in range(arr.shape[1]):
        if arr[a, b] > 0.1:
            uplist.append((a, b, arr[a, b]))
        elif arr[a, b] < -0.15:
            downlist.append((a, b, arr[a, b]))
print("月度涨幅高于10%的数值所在数组中的索引值以及对应的数据为：", uplist, "\n", "月度跌幅超过15%的数值所在数组中的索引值以及对应的数据为：", downlist)

#第三小题
print("小米集团的全部月度涨跌幅数据为", arr[3])
print("2019年5月全部股票的涨跌幅数据为", arr[:, 4])
print("平安好医生和腾讯控股在2019年2月至4月期间的月度涨跌幅数据为", "\n", arr[1:3, 1:4])

#第四小题
# arr.sort(axis=1)
# print("按照行对月度涨跌幅由小到大进行排序", "\n", arr)
# arr.sort(axis=0)
# print("按照列对月度涨跌幅由小到大进行排序", "\n", arr)
#上面这么些会导致按列的排序是在行的排序的基础上的
arr1 = np.sort(arr, 1)
arr2 = np.sort(arr, 0)
print("按照行对月度涨跌幅由小到大进行排序", "\n", arr1)
print("按照列对月度涨跌幅由小到大进行排序", "\n", arr2)