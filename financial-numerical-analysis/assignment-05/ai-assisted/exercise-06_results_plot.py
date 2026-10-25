# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Explicit AI-assisted source version; not claimed as independent work.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data = pd.read_table('MCSimulation_Jason_000021.txt')
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')
data = data.drop('close_price', axis=1)
print(data)
print(data.shape)

#出现了一个问题，数据库中的股票价格只到2018年，我们没有办法从数据库中读取得到000021的2019年上半年收盘价
#从resset上重新找到真实数据

data_real = pd.read_excel('exercise-06_closeprice_000021.xlsx')
data_real = data_real.ffill(axis=0)
data_real.columns = ['date', 'close_price']
data_real['date'] = pd.to_datetime(data_real['date'], format='%Y-%m-%d')
print(data_real)
print(data_real.shape)

data_draw = pd.merge(data, data_real, on='date', how='outer')
print(data_draw)
#以上为数据的整理，下面终于可以开始画图了

plt.figure(1)
plt.plot(data_draw['date'], data_draw['close_price'], '-k', lw=2)
plt.plot(data_draw['date'], data_draw['close_sim 1'], lw=1.5)
plt.plot(data_draw['date'], data_draw['close_sim 2'], lw=1.5)
plt.plot(data_draw['date'], data_draw['close_sim 3'], lw=1.5)
plt.plot(data_draw['date'], data_draw['close_sim 4'], lw=1.5)
plt.plot(data_draw['date'], data_draw['close_sim 5'], lw=1.5)

plt.xlabel(r"$t$", fontname='Times New Roman', fontsize=34)
plt.ylabel(r"$p(t)$", fontname='Times New Roman', fontsize=34)

xticks_ticks = pd.to_datetime(['2019-01-15', '2019-02-15', '2019-03-15', '2019-04-15', '2019-05-15', '2019-06-15',])
xticks_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
plt.xticks(ticks=xticks_ticks,
           labels=xticks_labels,
           fontsize=26,
           fontname='Times New Roman')
plt.yticks(ticks=np.linspace(5, 12, 5),
           fontsize=26,
           fontname='Times New Roman'
           )
plt.legend(['real price'], loc='upper left', fontsize=20)

plt.savefig('exercise-06_results_plot.eps', dpi=300, bbox_inches='tight')
plt.savefig('exercise-06_results_plot.jpg', dpi=300, bbox_inches='tight')

plt.show()