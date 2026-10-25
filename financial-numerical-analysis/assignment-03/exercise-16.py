# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
arr_amount = np.array(pd.read_excel("exercise-16_1.xlsx", sheet_name="交易额"))
name = arr_amount[:, 0]
print(name)
arr_amount = np.delete(arr_amount, 0, 1)
arr_amount = arr_amount.astype(float)
print(arr_amount)

arr_rate = np.array(pd.read_excel("exercise-16_1.xlsx", sheet_name="交易额变动比例"))
arr_rate = np.delete(arr_rate, 0, 1)
arr_rate = arr_rate.astype(float)
print(arr_rate)

#第二小题
for i in range(arr_amount.shape[0]):
    # print(name[i])
    print(name[i], "的累计交易额为", np.sum(arr_amount[i, :]), "亿元")

for i in range(arr_rate.shape[0]):
    # print(name[i])
    print("4/"+str(15+i)+"的累计交易额为", np.sum(arr_amount[:, i]), "亿元")

print("整个数组的累积交易额为", np.sum(arr_amount[:, :]), "亿元")

#第三小题
arr_amount_check = np.copy(arr_amount)
for a in range(arr_amount.shape[0]):
    for b in range(arr_amount.shape[1]):
        arr_amount[a, b] = np.log(arr_amount[a, b])
print("自然对数数组：\n", arr_amount)
print("针对以每个交易额自然对数结果作为元素的新数组，计算以e为底的指数次方：\n", np.e**arr_amount)


arr_amount = np.copy(arr_amount_check)
# print(arr_amount_check)
# print(arr_amount)
for a in range(arr_amount.shape[0]):
    for b in range(arr_amount.shape[1]):
        arr_amount[a, b] = np.log10(arr_amount[a, b])
print("底数10的对数数组：\n", arr_amount)

arr_amount = np.copy(arr_amount_check)
# print(arr_amount_check)
# print(arr_amount)
for a in range(arr_amount.shape[0]):
    for b in range(arr_amount.shape[1]):
        arr_amount[a, b] = np.log2(arr_amount[a, b])
print("底数2的对数数组：\n", arr_amount)
#注意运用np.copy可以真正地把一个常数和变量分离开，否则二者中一个改变另一个也会改变

#第四小题
for i in range(arr_rate.shape[0]):
   print(name[i]+"的累积变动比例为", np.prod(arr_rate[i, :]))