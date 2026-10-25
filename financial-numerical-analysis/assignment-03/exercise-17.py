# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
name = ["工商银行", "中国银行", "交通银行", "招商银行", "民生银行"]
print(name)
arr = np.array(pd.read_excel("exercise-17_1.xlsx"))
print(arr, "\n", arr.shape)
arr_cap = arr[4, 1:]
print(arr_cap)
arr_A_nap = arr[5:7, 1:]
arr_H_nap = arr[7:9, 1:]
print(arr_A_nap, "\n", arr_H_nap)

for i in range(arr_A_nap.shape[1]):
    print(name[i], "A股的每股净资产为", arr_A_nap[0, i]/arr_cap[i], "元")
for i in range(arr_A_nap.shape[1]):
    print(name[i], "A股的每股净利润为", arr_A_nap[1, i]/arr_cap[i], "元")
for i in range(arr_H_nap.shape[1]):
    print(name[i], "H股的每股净资产为", arr_H_nap[0, i]/arr_cap[i], "元")
for i in range(arr_H_nap.shape[1]):
    print(name[i], "H股的每股净利润为", arr_H_nap[1, i]/arr_cap[i], "元")

#第二小题
arr_A_finprice = arr[2, 1:]
print(arr_A_finprice)
arr_H_finprice = arr[3, 1:]
print(arr_H_finprice)

#PB（市净率） = 每股市价 / 每股净资产
#PE（市盈率） = 每股市价 / 每股收益
print(arr_A_nap)
for i in range(arr_cap.shape[0]):
    print(name[i], "的6月末A股的市净率（PB）为", arr_A_finprice[i]/(arr_A_nap[0, i]/arr_cap[i]))
    print(name[i], "的6月末A股的市盈率（PE）为", arr_A_finprice[i]/(arr_A_nap[1, i]/arr_cap[i]))

for i in range(arr_cap.shape[0]):
    print(name[i], "的6月末H股的市净率（PB）为", arr_H_finprice[i]/(arr_H_nap[0, i]/arr_cap[i]))
    print(name[i], "的6月末H股的市盈率（PE）为", arr_H_finprice[i]/(arr_H_nap[1, i]/arr_cap[i]))

#第三小题
arr_maxPBPE = np.zeros([2, 5])
arr_minPBPE = np.zeros([2, 5])
# print(arr_A_nap.shape)
for i in range(arr_cap.shape[0]):
    #maxPB
    if (arr_A_finprice[i]/(arr_A_nap[0, i]/arr_cap[i])) >= (arr_H_finprice[i]/(arr_H_nap[0, i]/arr_cap[i])):
        arr_maxPBPE[0, i] = arr_A_finprice[i]/(arr_A_nap[0, i]/arr_cap[i])
    else:
        arr_maxPBPE[0, i] = arr_H_finprice[i]/(arr_H_nap[0, i]/arr_cap[i])
    #maxPE
    if (arr_A_finprice[i]/(arr_A_nap[1, i]/arr_cap[i])) >= (arr_H_finprice[i]/(arr_H_nap[1, i]/arr_cap[i])):
        arr_maxPBPE[1, i] = arr_A_finprice[i]/(arr_A_nap[1, i]/arr_cap[i])
    else:
        arr_maxPBPE[1, i] = arr_H_finprice[i]/(arr_H_nap[1, i]/arr_cap[i])
print(arr_maxPBPE)

for i in range(arr_cap.shape[0]):
    #minPB
    if (arr_A_finprice[i]/(arr_A_nap[0, i]/arr_cap[i])) <= (arr_H_finprice[i]/(arr_H_nap[0, i]/arr_cap[i])):
        arr_minPBPE[0, i] = arr_A_finprice[i]/(arr_A_nap[0, i]/arr_cap[i])
    else:
        arr_minPBPE[0, i] = arr_H_finprice[i]/(arr_H_nap[0, i]/arr_cap[i])
    #minPE
    if (arr_A_finprice[i]/(arr_A_nap[1, i]/arr_cap[i])) <= (arr_H_finprice[i]/(arr_H_nap[1, i]/arr_cap[i])):
        arr_minPBPE[1, i] = arr_A_finprice[i]/(arr_A_nap[1, i]/arr_cap[i])
    else:
        arr_minPBPE[1, i] = arr_H_finprice[i]/(arr_H_nap[1, i]/arr_cap[i])
print(arr_minPBPE)

#第四小题
for i in range(arr_cap.shape[0]):
    print(name[i], "在6月末的市值为", 2000*arr_H_finprice[i], "万港元")

arr_H_rate_0702 = arr[9, 1:]
print(arr_H_rate_0702)

for i in range(arr_cap.shape[0]):
    print(name[i], "在7月2日的盈亏情况为", 2000*arr_H_finprice[i]*arr_H_rate_0702[i], "万港元")

for i in range(arr_cap.shape[0]):
    print(name[i], "在7月2日的H股收盘价为", arr_H_finprice[i]*(1 + arr_H_rate_0702[i]), "港元/股")