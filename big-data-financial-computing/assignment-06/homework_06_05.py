import numpy as np
import pandas as pd
import time
import requests
import re
import matplotlib.pyplot as plt
import statsmodels.api as sm


plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'

# url_base = 'https://guba.eastmoney.com/list,603569'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}
#
# p1 = r'<td.+?\s.+?read">(.+?)</div></td><td><div\s.+?reply">(.+?)</div></td><td><div\s.+?a\s.+?".+?"\s.+?".+?"\shref="(.+?)">(.+?)</a></div></td><td><div\s.+?=".+?"><a\s.+?".+?">(.+?)</a></div></td><td><div\s.+?"update">(\d{2}-\d{2}\s\d{2}:\d{2})</div>'
# objp = re.compile(p1, re.S)
#
# all_data = []
#
# for i in range(1, 21):
#     if i == 1:
#         url = url_base + '.html'
#     else:
#         url = url_base + '_' + str(i) + '.html'
#
#     while True:
#         try:
#             res = requests.get(url, headers=headers, timeout=10)
#             res.encoding = 'utf-8'
#             html = res.text
#             match = objp.findall(html)
#             all_data.extend(match)
#             if len(match) > 0:
#                     break
#         except:
#             print('failing to crawl the data because of timeout')
#         time.sleep(np.random.randint(10, 30))
#
# print(all_data)
# data = pd.DataFrame(all_data)
# # utf-8-sig确保excel正常显示中文
# data.to_csv("data_guba.csv", index=False, encoding='utf-8-sig')
# print(data)


data = pd.read_csv("data_guba.csv")
data.columns = ['views', 'replies', 'link', 'title', 'author', 'time']
data = data[['time', 'title', 'author', 'views', 'replies']]
print(data)
# data['time'] = pd.to_datetime(data['time'], format="%m-%d %H:%M")
# for i in range(len(data['time'])):
#     if data.iloc[i, 0] < pd.to_datetime('1900-05-22 00:00:00'):
#         data.iloc[i, 0] = pd.to_datetime("2026-"+str(data.iloc[i, 0]), format="%Y-%m-%d %H:%M")
#     else:
#         data.iloc[i, 0] = pd.to_datetime("2025-"+str(data.iloc[i, 0]), format="%Y-%m-%d %H:%M")
# 以上试图补全日期，但是太过复杂


month = data['time'].str[:2].astype(int)
day = data['time'].str[3:5].astype(int)
# 使用numpy的三目运算贴上年标签
# 若日期<5/22，就是 2026年（真值），反之为2025年（假值）
year = np.where((month < 5) | ((month == 5) & (day < 22)), 2026, 2025)
data['time'] = pd.to_datetime(year.astype(str) + '-' + data['time'], format='%Y-%m-%d %H:%M')
data = data.sort_values('time').reset_index(drop=True)
data.to_csv("data_v2.csv", index=False, encoding='utf-8-sig')
print(data)

# 读取收益率数据
data_price = pd.read_csv("data_sina_cjwl.txt", sep="\t")
print(data_price)
data_price['day'] = pd.to_datetime(data_price['day'])
data_price = data_price[data_price['day'] > pd.to_datetime("2025-08-25")].reset_index(drop=True)
data_price = data_price[['day', 'close', 'volume']]
# 把close转成数字
data_price['close'] = pd.to_numeric(data_price['close'], errors='coerce')
data_price['yield'] = np.log(data_price['close'])-np.log(data_price['close']).shift(1)
print(data_price)


# 读取中证1000指数
res = requests.get('http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh000852&scale=240&ma=no&datalen=10000')
data_json = res.json()
data_index = pd.DataFrame(data_json)
data_index['day'] = pd.to_datetime(data_index['day'])
data_index = data_index[data_index['day'] > pd.to_datetime("2025-08-25")].reset_index(drop=True)
data_index = data_index[['day', 'close', 'volume']]
# 把close转成数字
data_index['close'] = pd.to_numeric(data_index['close'], errors='coerce')
data_index['rm'] = np.log(data_index['close'])-np.log(data_index['close']).shift(1)
print(data_index)



# 开始构造指标
# dt是pandas的日期提取器，.date 只取"年月日
# agg=aggregate聚合：新列名=('原列名', '统计方法')
factor = data.groupby(data['time'].dt.date).agg(
    posts=('title', 'count'),           # 帖子数
    views=('views', 'sum'),             # 总浏览量
    replies=('replies', 'sum'),        # 总评论数
    avg_title_len=('title', lambda x: x.str.len().mean())  # 平均标题长度
    ).reset_index()
factor.columns = ['day', 'posts', 'views', 'replies', 'avg_len']
print(factor)



# 整合数据
data_reg = pd.merge(left=data_price[['day', 'volume', 'yield']],
                    right=data_index[['day', 'rm']],
                    on='day',
                    how='inner')
data_reg['r'] = data_reg['yield'] - data_reg['rm']
print(data_reg)

factor['day'] = pd.to_datetime(factor['day'])
data_reg = pd.merge(left=factor,
                    right=data_reg,
                    on='day',
                    how='inner')
print(data_reg)

# 8月27日数据可能截取不全，舍去
data_reg = data_reg.iloc[1:, :]

# 画图展示数据
plt.figure(1, figsize=(16, 12))
plt.title("长久物流2025/9-2026/5超额收益率、成交量、讨论热度", fontsize=24)
plt.subplot(3, 1, 1)
plt.plot(data_reg['day'], data_reg['r'])
plt.ylabel("超额收益率")
plt.subplot(3, 1, 2)
plt.bar(data_reg['day'], data_reg['volume'])
plt.ylabel("成交量")
plt.subplot(3, 1, 3)
plt.bar(data_reg['day'], data_reg['posts'])
# plt.bar(data_reg['day'], data_reg['views'])
# plt.bar(data_reg['day'], data_reg['replies'])
# plt.bar(data_reg['day'], data_reg['avg_len'])
plt.ylabel("帖子个数")
plt.xlabel("时间")
plt.savefig('长久物流超额收益率、成交量、讨论热度（2025年9月-2026年5月）.jpg', dpi=300, bbox_inches='tight')
# plt.show()



# 开始回归
data_reg['posts'] = data_reg['posts'].shift(1)
data_reg['views'] = data_reg['views'].shift(1)
data_reg['replies'] = data_reg['replies'].shift(1)
data_reg['avg_len'] = data_reg['avg_len'].shift(1)
data_reg = data_reg.dropna()
print(data_reg)

# y = data_reg['r']
y = np.abs(data_reg['r'])
X = data_reg[['posts', 'views', 'replies', 'avg_len']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()   # 最小二乘回归
print(model.summary())

y = data_reg['volume']
X = data_reg[['posts', 'views', 'replies', 'avg_len']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()   # 最小二乘回归
print(model.summary())