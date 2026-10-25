# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data = pd.read_table('Exp04-Python-实验数据-余额宝历史收益.txt', sep='\t', encoding='GB2312')
print(data.columns)
# print(data)
print(data.shape)

fund_time = pd.to_datetime(data['日期'][-1::-1], format='%Y-%m-%d')
# print(fund_time)
fund_time.reset_index(drop=True, inplace=True)
# print(fund_time)

fund_rateper10000 = data['万份收益'][-1::-1]
fund_rateper10000.reset_index(drop=True, inplace=True)
# print(fund_rateper10000)
#读取数据，重置索引

addpoint_time = pd.to_datetime(['2013-06-19', '2014-09-02', '2015-10-17', '2016-10-02', '2017-05-30', '2019-05-30', '2020-08-31'],
                               format='%Y-%m-%d')
addpoint_amount = [13000, 5000, 8000, 10000, 9000, 2000, 1000]
addpoint = {}
for i in range(7):
    addpoint[addpoint_time[i]] = addpoint_amount[i]
print(addpoint)
#构造加仓字典

# time = list(fund_time)
amount_profitbase = []
new_profitbase = 0
for a in range(3059):
    new_profitbase += np.round(new_profitbase / 10000 * fund_rateper10000[i], 2)
    for b in range(7):
        if fund_time[a] == addpoint_time[b]:
            new_profitbase += addpoint[fund_time[a]]
            # print(fund_rateper10000[i])
            # print(new_profitbase)
            # print("addddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        # else:
            # print(fund_rateper10000[i])
            # print(new_profitbase)
    amount_profitbase.append(float("{:.2f}".format(new_profitbase)))
print(amount_profitbase, len(amount_profitbase))
#去尾保留两位小数似乎比较困难，可以通过np.flour和"{:.2f}".format来实现,最后通过float再变回float型
#计算累计金额

amount_profitbase = np.array(amount_profitbase)
amount_profitbase = np.reshape(amount_profitbase, (3059, 1))
print(amount_profitbase.shape)
#使得金额形状与时间一样

a = 0
b = 0
for i in fund_time:
    if i < pd.to_datetime(['2013-06-18'], format='%Y-%m-%d'):
        fund_time = np.delete(fund_time, 1, 0)
        a += 1
    if i >pd.to_datetime(['2021-10-05'], format='%Y-%m-%d'):
        fund_time = np.delete(fund_time, 1, 0)
        b += 1
print(fund_time, "\n", fund_time.shape)
print(a, b)
for i in range(a):
    amount_profitbase = np.delete(amount_profitbase, i, 0)
for i in range(1, b+1, 1):
    amount_profitbase = np.delete(amount_profitbase, -i, 0)
# print(amount_profitbase, amount_profitbase.shape)
#掐头去尾

plt.xlim(pd.to_datetime(['2013', '2021'], format='%Y'))
plt.xticks(ticks=pd.to_datetime(['2013', '2015', '2017', '2019', '2021'], format='%Y'),
           labels=['2013', '2015', '2017', '2019', '2021'],
           fontsize=18,
           fontname='Times New Roman')
plt.ylim(10000, 60000)
plt.yticks(ticks=np.arange(10000, 60001, 10000),
           labels=np.arange(10000, 60001, 10000),
           fontsize=18,
           fontname='Times New Roman')
plt.xlabel(r'$time$', fontsize=30, fontname='Times New Roman')
plt.ylabel(r'$money$', fontsize=30, fontname='Times New Roman')
plt.plot(fund_time, amount_profitbase, '-k', lw=2)
#细节标注

y_mark = 0
y_mark_delta = 0
for i in range(7):
    y_mark += addpoint_amount[i]
    plt.text(addpoint_time[i], y_mark+y_mark_delta, str(addpoint_amount[i]))
    y_mark_delta += 1200
#在新购支付宝时间点对应的资金曲线附近，用文本标注购入支付宝XX元

plt.savefig('exercise-06.jpg', dpi=300, bbox_inches='tight')
plt.show()
#保存
