# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
name_of_security = "中芯国际"
security_code = "688981"
listing_date = "20200716"
listing_exchange = "上海证券交易所"
registered_capital = 7695363013
number_of_issuances = 1938463000
issue_price = 27.46
closing_price20200911 = 55.23
price_inflation = 5.36

#第二小题：
tuple1 = (name_of_security, security_code, listing_date, listing_exchange, registered_capital, number_of_issuances, issue_price, closing_price20200911, price_inflation)
print("元组首个元素："+tuple1[0])
print("元组最后一个元素：", tuple1[-1])
print("元组第3-6个元素：", tuple1[2:6])

#第三小题：
closing_price20200911_HK = 19.48
price_inflation_HK = 6.8
#元组不能直接增加元素，需要先变为列表
list1 = list(tuple1)
list1.append(closing_price20200911_HK)
list1.append(price_inflation_HK)
tuple2 = tuple(list1)
print(tuple2)
