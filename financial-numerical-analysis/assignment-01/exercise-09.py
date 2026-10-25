# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
stockname = ["中信证券", "国泰君安", "海通证券", "华泰证券", "广发证券", "招商证券", "申万宏源", "国信证券", "中信建投", "中国银河"]
print("证券公司A股证券名称的列表的个数为", len(stockname))
stocknamewithindex = []

n = 0
while n <= 9:
    stocknamewithindex.append([n+1, stockname[n]])
    n += 1
print(stocknamewithindex)

#第二小题：
netprofit = [98.7643, 70.7004, 57.7071, 51.6089, 46.3205, 44.4626, 42.4781, 34.3125, 31.0343, 29.3174]
n = 0
totalprofit = 0
while n <= 9:
    totalprofit += netprofit[n]
    n += 1
print("10家公司净利润的总和为", totalprofit, "亿元")

avgprofit = totalprofit/len(netprofit)
print("10家公司净利润的平均值为", avgprofit, "亿元")

#第三小题：
PCT = [54.7783, 31.5274, 59.4318, 38.3333, 27.5237, 30.7463, 35.6265, 61.7682, 193.3410, 73.4604]
endprice = [27.78, 20.15, 14.03, 22.41, 16.17, 17.52, 5.52, 13.54, 25.55, 11.83]
# print(len(PCT), len(endprice))
print("最大涨幅为", max(PCT), "%")
print("最小涨幅为", min(PCT), "%")
endprice.sort()
print("对收盘价价列表按价格从低到高排序：", endprice)

#第四小题：
import pickle
#注意到python在遇到以0开头的数字室会报错，故股票代码应当以字符串表示
stockcode = ["600030", "601211", "600837", "01688", "000776", "600999", "000166", "002736", "601066", "601881"]
list_tuple = []
n = 0
while n <= 9:
    tuple = {stockcode[n], stockname[n], netprofit[n], PCT[n], endprice[n]}
    list_tuple.append(tuple)
    n += 1
print(list_tuple)
output = open('exercise-09_4.pkl', 'wb')
pickle.dump(list_tuple, output, -1)
output.close()

#第五小题：
stock_amount = 10000000//(22.45*100)
print("可以买入", stock_amount, "手股票")