# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
arr = np.array(pd.read_excel("exercise-15_1.xlsx"))
print(arr)
for i in range(arr.shape[0]):
    print(arr[i, 0], "的最大市盈率为", np.max(arr[i, 2:]))
    print(arr[i, 0], "的最小市盈率为", np.min(arr[i, 2:]))
#注意这里得把字符串和股票代码排除
for i in range(2, arr.shape[1]):
    print("19/5/"+str(25+i)+"的最大市盈率为", np.max(arr[0:, i]))
    print("19/5/"+str(25+i)+"的最小市盈率为", np.min(arr[0:, i]))
print("整个数组的最大市盈率为", np.max(arr[:, 2:]))
print("整个数组的最小市盈率为", np.min(arr[:, 2:]))

#第二小题
for i in range(arr.shape[0]):
    print(arr[i, 0], "的平均市盈率为", np.mean(arr[i, 2:]))

for i in range(2, arr.shape[1]):
    print("19/5/"+str(25+i)+"的平均市盈率为", np.mean(arr[0:, i]))

print("整个数组的平均市盈率为", np.mean(arr[:, 2:]))

#第三小题
for i in range(arr.shape[0]):
    print(arr[i, 0], "的市盈率方差为", np.var(arr[i, 2:]))
    print(arr[i, 0], "的市盈率标准差为", np.std(arr[i, 2:]))

for i in range(2, arr.shape[1]):
    print("19/5/"+str(25+i)+"的市盈率方差为", np.var(arr[0:, i]))
    print("19/5/"+str(25+i)+"的市盈率标准差为", np.std(arr[0:, i]))

print("整个数组的市盈率方差为", np.var(arr[:, 2:]))
print("整个数组的市盈率标准差为", np.std(arr[:, 2:]))
