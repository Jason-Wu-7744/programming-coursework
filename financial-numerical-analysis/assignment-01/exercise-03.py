# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
list1_name = ["道琼斯工业指数", "纳斯达克指数", "标普500指数", "罗素3000指数", "上证指数", "深圳成指"]
list2_price = [27665.64, 10853.55, 3340.94, 1946.98, 3260.35, 4627.28]
print(list1_name[2], list1_name[-2])
print("10853.55的索引值为：", list2_price.index(10853.55))
print("4627.28的索引值为：", list2_price.index(4627.28))

#第二小题：
list3_name = ["英国富时100", "法国CAC40", "德国DAX", "俄罗斯MOEX"]
list4_price = [6032.09, 5034.14, 13202.84, 3315.81]
list1_name = list1_name + list3_name
list2_price = list2_price + list4_price
print(list1_name, "\n", list2_price)

#第三小题
luosu300_index = list1_name.index("罗素3000指数")
# print(luosu300_index)
list1_name.remove("罗素3000指数")
del list2_price[3]
# print(list1_name, "\n", list2_price)
list1_name.insert(6, "印度SENSEX30指数")
list2_price.insert(6, 38854.55)
print(list1_name, "\n", list2_price)

#第四小题
list2_price.sort(reverse = True)
print(list2_price)
list2_price.sort()
print(list2_price)
list1_name =[]
list2_price = []
del list1_name
del list2_price