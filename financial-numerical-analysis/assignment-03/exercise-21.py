# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
def normal_pdf(x, u, sigma):
    return 1/((2*np.pi)**(1/2)*sigma)*np.e**(-(x-u)**2/(2*sigma**2))
def normal_pdf_stats(u, sigma):
    return u, sigma
print(normal_pdf(2, 0, 1))

def lognormal_pdf(x, u, sigma):
    if x <= 0:
        return "x应>0"
    else:
        return 1 / ((2 * np.pi) ** (1 / 2) * sigma * x) * np.e ** (-(np.log(x) - u) ** 2 / (2 * sigma ** 2))
def lognormal_pdf_stats(u, sigma):
    return np.e**(u+sigma**2/2), (np.e**(sigma**2)-1)*np.e**(2*u+sigma**2)
print(lognormal_pdf(np.e, 1, np.e))

#第二小题
arr_you = np.array(pd.read_excel("exercise-21_1.xlsx", sheet_name="中国石油"))
arr_hua = np.array(pd.read_excel("exercise-21_1.xlsx", sheet_name="中国石化"))
# print(arr_you, arr_hua)
date = arr_you[:, 0]
# print(date)
arr_you = np.delete(arr_you, 0, 1)
arr_you = arr_you.astype(float)
# print(arr_you, arr_you.dtype)
arr_you_finprice = arr_you[:, 0]
arr_you_rate = arr_you[:, 1]
arr_hua = np.delete(arr_hua, 0, 1)
arr_hua = arr_hua.astype(float)
# print(arr_hua, arr_hua.dtype)
arr_hua_finprice = arr_hua[:, 0]
arr_hua_rate = arr_hua[:, 1]

print("中国石油的股票收盘价数组：\n", arr_you_finprice)
print("中国石油的股票价格涨跌幅数组：\n", arr_you_rate)
print("中国石化的股票收盘价数组：\n", arr_hua_finprice)
print("中国石化的股票价格涨跌幅数组：\n", arr_hua_rate)

arr_you_finprice_mean = np.mean(arr_you_finprice)
print("中国石油的股票收盘价的均值：", arr_you_finprice_mean)
arr_you_finprice_std = np.std(arr_you_finprice)
print("中国石油的股票收盘价的标准差：", arr_you_finprice_std)
arr_you_rate_mean = np.mean(arr_you_rate)
print("中国石油的股票价格涨跌幅的均值：", arr_you_rate_mean)
arr_you_rate_std = np.std(arr_you_rate)
print("中国石油的股票价格涨跌幅的标准差：", arr_you_rate_std)

arr_hua_finprice_mean = np.mean(arr_hua_finprice)
print("中国石化的股票收盘价的均值：", arr_hua_finprice_mean)
arr_hua_finprice_std = np.std(arr_hua_finprice)
print("中国石化的股票收盘价的标准差：", arr_hua_finprice_std)
arr_hua_rate_mean = np.mean(arr_hua_rate)
print("中国石化的股票价格涨跌幅的均值：", arr_hua_rate_mean)
arr_hua_rate_std = np.std(arr_hua_rate)
print("中国石化的股票价格涨跌幅的标准差：", arr_hua_rate_std)

#第三小题
print("以中国石油的价格涨跌幅的均值和标准差为准：")
you_samples = np.random.normal(arr_you_rate_mean, arr_you_rate_std, 10000)
you_samples_mean = np.mean(you_samples)
you_samples_std = np.std(you_samples)
print("均值：", you_samples_mean, "标准差：", you_samples_std)

print("以中国石化的价格涨跌幅的均值和标准差为准：")
hua_samples = np.random.normal(arr_hua_rate_mean, arr_hua_rate_std, 10000)
hua_samples_mean = np.mean(hua_samples)
hua_samples_std = np.std(hua_samples)
print("均值：", hua_samples_mean, "标准差：", hua_samples_std)

#第四小题
#通过e, var倒算出u和sigma
print("以中国石油的收盘价的均值和标准差为准：")
you_var = arr_you_finprice_std**2
you_e = arr_you_finprice_mean
you_sigma = np.sqrt(np.log(you_var/you_e**2+1))
you_u = np.log(you_e) - you_sigma**2/2
print("中国石油股票价格的自然对数所服从正态分布的期望值为", you_u, "标准差为", you_sigma)

print("以中国石化的收盘价的均值和标准差为准：")
hua_var = arr_hua_finprice_std**2
hua_e = arr_hua_finprice_mean
hua_sigma = np.sqrt(np.log(hua_var/hua_e**2+1))
hua_u = np.log(hua_e) - hua_sigma**2/2
print("中国石化股票价格的自然对数所服从正态分布的期望值为", hua_u, "标准差为", hua_sigma)

#第五小题
print("以中国石油的收盘价的均值和标准差为准：")
you_samples = np.random.lognormal(you_u, you_sigma, 10000)
you_samples_mean = np.mean(you_samples)
you_samples_std = np.std(you_samples)
print("均值：", you_samples_mean, "标准差", you_samples_std)

print("以中国石化的收盘价的均值和标准差为准：")
hua_samples = np.random.lognormal(hua_u, hua_sigma, 10000)
hua_samples_mean = np.mean(hua_samples)
hua_samples_std = np.std(hua_samples)
print("均值：", hua_samples_mean, "标准差", hua_samples_std)

#可以看出收益率本身就服从正态分布，可以直接用样本的均值标准差作为抽样的参数
#股票价格服从对数正态分布，其均值与方差不能用股票价格样本的均值和方差，而是要倒算出真正的对数正态分布的参数。