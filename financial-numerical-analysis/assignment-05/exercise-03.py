# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

#由于是日度数据，所以可以用涨跌幅来近似收益率
data = pd.read_excel('exercise-03_1.xlsx', index_col=0)
# print(data)

#第一小题
yield_daily = data['涨跌幅(%)_ChgPct']
# print(yield_daily)

plt.figure(1)
plt.plot(pd.to_datetime(yield_daily.index, format='%Y-%m-%d'), yield_daily.iloc[:])
plt.xticks(['2018', '2019', '2020'])
plt.xlabel(r'$time$')
plt.ylabel(r'$yield$')
plt.title(r'$yield$')
plt.savefig('exercise-03_yield.jpg', dpi=600, bbox_inches='tight')


#第二小题
amount_daily = data['成交金额(元)_TrdSum']
# print(amount_daily)

plt.figure(2)
plt.hist(amount_daily, bins=300)
plt.xlabel(r'$amount$')
plt.ylabel(r'$amountofdays$')
plt.title(r'$amountbyhist$')
plt.savefig('exercise-03_amount_hist.jpg', dpi=600, bbox_inches='tight')

#第三小题
plt.figure(3)
plt.boxplot(amount_daily, vert=False)
plt.xlabel(r'$amount$')
plt.title(r'$amountbyboxplot$')
plt.savefig('exercise-03_amount_boxplot.jpg', dpi=600, bbox_inches='tight')

#第四小题
price_daily = data.iloc[:, 0:4]
# print(price_daily)
opening_price_daily = data['开盘价(元/点)_OpPr']
closing_price_daily = data['收盘价(元/点)_ClPr']
highest_price_daily = data['最高价(元/点)_HiPr']
lowest_price_daily = data['最低价(元/点)_LoPr']

plt.figure(4)
plt.subplot(2, 2, 1)
plt.plot(pd.to_datetime(yield_daily.index, format='%Y-%m-%d'), opening_price_daily.iloc[:])
plt.xticks([])
plt.yticks([2500, 3000, 3500], fontsize=12)
# plt.xlabel(r'$time$')
plt.ylabel(r'$price$')
plt.title(r'$openingprice$')

plt.subplot(2, 2, 2)
plt.plot(pd.to_datetime(yield_daily.index, format='%Y-%m-%d'), closing_price_daily.iloc[:])
plt.xticks([])
plt.yticks([])
# plt.xlabel(r'$time$')
# plt.ylabel(r'$price$')
plt.title(r'$closingprice$')

plt.subplot(2, 2, 3)
plt.plot(pd.to_datetime(yield_daily.index, format='%Y-%m-%d'), highest_price_daily)
plt.xticks(['2018', '2019', '2020'], fontsize=8)
plt.yticks([2500, 3000, 3500], fontsize=12)
plt.xlabel(r'$time$')
plt.ylabel(r'$price$')
plt.title(r'$highestprice$')

plt.subplot(2, 2, 4)
plt.plot(pd.to_datetime(yield_daily.index, format='%Y-%m-%d'), lowest_price_daily.iloc[:])
plt.xticks(['2018', '2019', '2020'], fontsize=8)
plt.yticks([])
plt.xlabel(r'$time$')
# plt.ylabel(r'$price$')
plt.title(r'$lowestprice$')

plt.savefig('exercise-03_price.jpg', dpi=600, bbox_inches='tight')

plt.show()