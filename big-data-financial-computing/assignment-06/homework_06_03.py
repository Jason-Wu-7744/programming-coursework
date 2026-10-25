import numpy as np
import pandas as pd
import time
import requests
import re

# url = 'https://finance.sina.com.cn/roll/c/56592.shtml?page='
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}
# res = requests.get(url, headers=headers)
# html = res.text
# p1 = r'<td.+?\s.+?read">(.+?)</div></td><td><div\s.+?reply">(.+?)</div></td><td><div\s.+?a\s.+?".+?"\s.+?".+?"\shref="(.+?)">(.+?)</a></div></td><td><div\s.+?=".+?"><a\s.+?".+?">(.+?)</a></div></td><td><div\s.+?"update">(\d{2}-\d{2}\s\d{2}:\d{2})</div>'
#
# while True:
#     try:
#         mcheck = re.findall(p1, html, re.S)
#         if len(mcheck.group()) > 0:
#             html = mcheck.group()
#             break
#     except:
#         print('failing to crawl the data because of timeout')
#     time.sleep(np.random.randint(10, 30))
#
# fw = open('data603569.csv', 'w')



# 更换手机热点后可以避免反爬被返回第一页

def myfun_crawl_guba_603569():
    url_base = 'https://guba.eastmoney.com/list,603569'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}

    p1 = r'<td.+?\s.+?read">(.+?)</div></td><td><div\s.+?reply">(.+?)</div></td><td><div\s.+?a\s.+?".+?"\s.+?".+?"\shref="(.+?)">(.+?)</a></div></td><td><div\s.+?=".+?"><a\s.+?".+?">(.+?)</a></div></td><td><div\s.+?"update">(\d{2}-\d{2}\s\d{2}:\d{2})</div>'
    objp = re.compile(p1, re.S)

    fw = open('data_guba_cjwl.txt', 'w', encoding='utf-8')
    fw.write('{:<18}{:<18s}{:<6s}{:<6s}{:s}\t{:s}\n'.format("作者", "时间", "阅读量", "评论数", "标题", "链接"))
    # 爬取1-20页
    # 加入一个字符串确保不会反爬返回第一页
    last_title = ''
    for i in range(1, 21):
        if i == 1:
            url = url_base + '.html'
        else:
            url = url_base + '_' + str(i) + '.html'

        while True:
            try:
                res = requests.get(url, headers=headers, timeout=10)
                res.encoding = 'utf-8'
                html = res.text
                match = objp.findall(html)
                if len(match) > 0:
                    # 【新增】检查是否被反爬返回了重复内容
                    if i > 1 and match[0][3] == last_title:
                        print(f'第{i}页疑似重复，10秒后重试...')
                        time.sleep(10)
                        continue
                    last_title = match[0][3]  # 【新增】更新记录
                    break
            except:
                print('failing to crawl the data because of timeout')
            time.sleep(np.random.randint(10, 30))

        for line in match:
            # 输出顺序：作者、时间、阅读量、评论数、标题、链接
            fw.write('{:<18s}{:<18s}{:<6s}{:<6s}{:s}\t{:s}\n'.format(line[4], line[5], line[0], line[1], line[3], line[2]))
    fw.close()

myfun_crawl_guba_603569()