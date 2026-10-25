# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
#上一题中出现了太多变量名，下面不妨开始使用字典
stockchange = {"2019-03-19": 1000000, "2019-03-20": 5000000, "2019-03-21": 2000000, "2019-03-22": 8000000, "2019-03-25": 3000000, "2019-03-26": -2000000, "2019-03-27": -5000000, "2019-03-28": -3000000, "2019-03-29": -4000000, "2019-04-01": 0, "2019-04-02": 0, "2019-04-03": 0, "2019-04-04": 0, "2019-04-08": 0}
#股市周末休市，有时日期不连续
# print(stockchange["2019-03-27"])
stockprice = {"2019-03-19": 75.35, "2019-03-20": 76.55, "2019-03-21": 75.80, "2019-03-22": 74.72, "2019-03-25": 72.29, "2019-03-26": 72.69, "2019-03-27": 74.22, "2019-03-28": 73.40, "2019-03-29": 77.10, "2019-04-01": 78.60, "2019-04-02": 78.96, "2019-04-03": 79.86, "2019-04-04": 80.20, "2019-04-08": 80.59}
stocknum = stockchange["2019-03-19"]
stocknum += stockchange["2019-03-20"]
stocknum += stockchange["2019-03-21"]
stocknum += stockchange["2019-03-22"]
stocknum += stockchange["2019-03-25"]
stocknum += stockchange["2019-03-26"]
stocknum += stockchange["2019-03-27"]
stocknum += stockchange["2019-03-28"]
stocknum += stockchange["2019-03-29"]
stocknum += stockchange["2019-04-01"]
stocknum += stockchange["2019-04-02"]
stocknum += stockchange["2019-04-03"]
stocknum += stockchange["2019-04-04"]
stocknum += stockchange["2019-04-08"]

print("截止至2019年3月29日该基金持有的中国平安A股股票的数量为", stocknum)

#第二小题：
stockrise = {"2019-03-19": 0.4667, "2019-03-20": 1.5926, "2019-03-21": -0.9798, "2019-03-22": -1.4248, "2019-03-25": -3.2521, "2019-03-26": 0.5533, "2019-03-27": 2.1048, "2019-03-28": -1.1048, "2019-03-29": 5.0409, "2019-04-01": 1.9455, "2019-04-02": 0.4580, "2019-04-03": 1.1398, "2019-04-04": 0.4257, "2019-04-08": 0.4863}
stockvalue = stocknum
stockvalue *= stockprice["2019-04-08"]
print("4月8日收盘后该基金持有中国平安A股股票的市值为", stockvalue, "元")

#下面使用收益率来复核
stockvalue_check = stocknum*stockprice["2019-03-29"]
stockvalue_check *= (stockrise["2019-04-01"]/100 + 1)
stockvalue_check *= (stockrise["2019-04-02"]/100 + 1)
stockvalue_check *= (stockrise["2019-04-03"]/100 + 1)
stockvalue_check *= (stockrise["2019-04-04"]/100 + 1)
stockvalue_check *= (stockrise["2019-04-08"]/100 + 1)
print("4月8日收盘后该基金持有中国平安A股股票的市值为", stockvalue_check, "元")
#两个结果十分相近，可以初步认为结果无误

#第三小题：
del stockprice["2019-04-01"]
del stockprice["2019-04-02"]
del stockprice["2019-04-03"]
del stockprice["2019-04-04"]
del stockprice["2019-04-08"]
stockprice_march = stockprice.values()
# print(stockprice_march)

if (75.81 in stockprice_march) == 1:
    print("75.81元属于2019年3月19日至3月29日中国平安A股的收盘价")
else:
    print("75.81元不属于2019年3月19日至3月29日中国平安A股的收盘价")
if (72.29 in stockprice_march) == 1:
    print("72.29元属于2019年3月19日至3月29日中国平安A股的收盘价")
else:
    print("72.29元不属于2019年3月19日至3月29日中国平安A股的收盘价")
if (72.45 in stockprice_march) == 1:
    print("72.45元属于2019年3月19日至3月29日中国平安A股的收盘价")
else:
    print("72.45元不属于2019年3月19日至3月29日中国平安A股的收盘价")