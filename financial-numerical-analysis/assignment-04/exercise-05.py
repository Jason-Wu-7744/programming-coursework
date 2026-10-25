# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

#上半部分
data = pd.read_table('Exp04-Python-实验数据-600000_2012-12-18.txt', sep = ",", encoding="GB2312")
# print(data)
print(data.columns)
data.columns = data.columns.str.strip()
print(data.columns)

stock_time = pd.to_datetime(data['成交时间'][-1::-1], format='%H:%M:%S')
print(stock_time)
stock_time.reset_index(drop=True, inplace=True)
print(stock_time)

stock_price = data['成交价'][-1::-1]
stock_price.reset_index(drop=True, inplace=True)

stock_volume = data['成交量(手)'][-1::-1]
stock_volume.reset_index(drop=True, inplace=True)

noon_time = pd.to_datetime('12:00:00', format='%H:%M:%S')
ind_morning = stock_time < noon_time
ind_afternoon = stock_time > noon_time

plt.figure(1)
plt.axes([0.2, 0.52, 0.7, 0.4])
plt.plot(stock_time.loc[ind_morning], stock_price[ind_morning], '-k', lw=0.5)
plt.plot(stock_time.loc[ind_afternoon], stock_price[ind_afternoon], '-m', lw=0.5)

plt.plot(pd.to_datetime(['09:30', '15:00'], format='%H:%M'), [9.07, 9.07], '-r', lw=2)
plt.xlim(pd.to_datetime(['09:40', '15:00'], format='%H:%M'))
plt.xticks(ticks=pd.to_datetime(['9:30', '10:30', '11:30', '13:00', '14:00', '15:00'], format='%H:%M'),
           labels=[],
           fontsize=18)
plt.yticks(ticks=np.arange(8.9, 9.4, 0.1), fontsize=18)
plt.ylabel(r'$p$', fontsize=24)
plt.text(pd.to_datetime('11:00', format='%H:%M'), 9.02, 'close price on Dec 17, 2012', fontsize=18)
plt.title('The transaction history of 600000 on Dec 18, 2012', fontsize=15)

plt.axes([0.2, 0.2, 0.7, 0.27])
plt.plot(stock_time.loc[ind_morning], stock_volume[ind_morning], '-c', lw=0.5)
plt.plot(stock_time.loc[ind_afternoon], stock_volume[ind_afternoon], '-b', lw=0.5)
plt.xlim(pd.to_datetime(['09:30', '15:00'], format="%H:%M"))
plt.xticks(ticks=pd.to_datetime(['9:30', '10:30', '11:30', '13:00', '14:00', '15:00'], format='%H:%M'),
           labels=['9:30', '10:30', '11:30', '13:00', '14:00', '15:00'],
           fontsize=18)
plt.xlabel(r'$t$', fontsize=24)
plt.yticks(ticks=np.arange(0, 30001, 10000),
           labels=[0, '1E4', '2E4', '3E4'],
           fontsize=18)
plt.ylabel(r'$v$', fontsize=24)

plt.savefig('Fig_600000_TranHis_20121218.jpg', dpi=300, bbox_inches='tight')
plt.show()