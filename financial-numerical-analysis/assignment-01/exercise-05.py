# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
dict1_USD_RMB = {"date": "2020-08-28", "midprice": 6.8654, "pricelimit": -0.42}
dict2_EUR_RMB = {"date": "2020-08-20", "midprice": 8.2048, "pricelimit": 0.07}
dict3_HKD_RMB = {"date": "2020-08-18", "midprice": 0.8926, "pricelimit": -0.16}
dict4_GBP_RMB = {"date": "22020-08-07", "midprice": 9.0959, "pricelimit": -0.45}

list1 = dict1_USD_RMB.keys()
print(list1)
list2 = dict3_HKD_RMB.values()
print(list2)
print(dict3_HKD_RMB.items())

#第二小题：
print("美元兑人民币汇率的具体日期为：", dict1_USD_RMB.get("date"))
print("欧元兑人民币汇率的中间价为", dict2_EUR_RMB.get("midprice"))
print("英镑兑人民币的涨跌幅为", dict4_GBP_RMB.get("pricelimit"))

#第三小题：
dict2_EUR_RMB["date"] = "2020-08-28"
dict2_EUR_RMB["midprice"] = 8.2048
dict2_EUR_RMB["pricelimit"] = 0.07
# print(dict2_EUR_RMB)

#第四小题：
dict3_HKD_RMB["midprice_yesterday"] = 0.8940
dict3_HKD_RMB["pricelimit_yesterday"] = -0.25
del dict4_GBP_RMB["pricelimit"]
# print(dict3_HKD_RMB, dict4_GBP_RMB)