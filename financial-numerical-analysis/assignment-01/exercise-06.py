# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
#第一小题：
stockchange_190415 = 50000
stockchange_190416 = 80000
stockchange_190417 = -40000
stockchange_190418 = 30000
stockchange_190419 = -60000

closing_price_190415 = 6.29
closing_price_190416 = 6.50
closing_price_190417 = 6.47
closing_price_190418 = 6.39
closing_price_190419 = 6.42

stockamount_190415 = stockchange_190415
stockamount_190416 = stockamount_190415 + stockchange_190416
# print(stockamount_190416)
stockamount_190417 = stockamount_190416 + stockchange_190417
# print(stockamount_190417)
stockamount_190418 = stockamount_190417 + stockchange_190418
# print(stockamount_190418)
stockamount_190419 = stockamount_190418 + stockchange_190419
# print(stockamount_190419)

stockvalue_190415 = stockamount_190415*closing_price_190415
stockvalue_190416 = stockamount_190416*closing_price_190416
stockvalue_190417 = stockamount_190417*closing_price_190417
stockvalue_190418 = stockamount_190418*closing_price_190418
stockvalue_190419 = stockamount_190419*closing_price_190419
# print(stockvalue_190419)

print("王先生在4月19日收盘以后按照最新收盘价计算所持有交通银行A股股票的市值为：", stockvalue_190419, "元")

#要算总盈亏金额（含浮动盈亏）就要拿卖掉的获得的收益-买的成本+手上持有的市值
profitfromsell = -stockchange_190417*closing_price_190417 - stockchange_190419*closing_price_190419
# print(profitfromsell)
costbybuy = stockchange_190415*closing_price_190415 + stockchange_190416*closing_price_190416 + stockchange_190418*closing_price_190418
# print(costbybuy)
allprofit = profitfromsell - costbybuy + stockvalue_190419
print("王先生在4月19日收盘以后按照最新收盘价计算所持有交通银行A股股票的总盈亏金额", allprofit, "元")

#第二小题：
Arithmetic_mean = (closing_price_190419 - closing_price_190415)/closing_price_190419/4
# print(Arithmetic_mean)
str_Arithmetic_mean = format(Arithmetic_mean, '.4%')
print("算术平均计算交通银行A股在4月16日至4月19日的平均日涨跌幅为", str_Arithmetic_mean)

Geometric_mean = (closing_price_190419/closing_price_190415)**(1/4) - 1
# print(Geometric_mean)
str_Geometric_mean = format(Geometric_mean, '.4%')
print("几何平均计算交通银行A股在4月16日至4月19日的平均日涨跌幅为", str_Geometric_mean)

#第三小题：
extramoney = 700000
closing_price_190422 = 6.11
stockamount_190422_hand = extramoney//(closing_price_190422*100)
print("王先生可购买", stockamount_190422_hand, "手股票")
remaining_money = extramoney % (closing_price_190422*100)
print("交易完成后账户资金余额是", remaining_money, "元")