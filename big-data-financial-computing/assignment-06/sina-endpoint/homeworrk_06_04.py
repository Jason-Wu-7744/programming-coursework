import numpy as np
import pandas as pd
import time
import requests
import re

res = requests.get("http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh603569&scale=240&ma=no&datalen=10000")
data_json = res.json()

data_603569 = pd.DataFrame(data_json)
print(data_603569)

# fw = open("data_sina_cjwl.txt", 'w', encoding="utf-8")
# # utf-8确保中文正常显示
# fw.write("{:<18s}\t{:<8s}\t{:<8s}\t{:<8s}\t{:<8s}\t{:<12s}\n".format("day", "open", "high", "low", "close", "volume"))
# for i in range(len(data_603569['day'])):
#     fw.write("{:<18s}\t{:<8s}\t{:<8s}\t{:<8s}\t{:<12s}\n"
#              .format(data_603569.iloc[i, 0], data_603569.iloc[i, 1], data_603569.iloc[i, 2],
#                      data_603569.iloc[i, 3], data_603569.iloc[i, 4], data_603569.iloc[i, 5]))
# fw.close()

fw = open('data_sina_cjwl.txt', 'w')
fw.write("{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\n".format("day", "open", "high", "low", "close", "volume"))
for i in range(len(data_json)):
    dj = data_json[i]
    fw.write('{:s}\t{:s}\t{:s}\t{:s}\t{:s}\t{:s}\n'.format(dj['day'], dj['open'], dj['high'], dj['low'], dj['close'], dj['volume']))
fw.close()