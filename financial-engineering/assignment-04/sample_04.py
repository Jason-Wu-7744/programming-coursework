import numpy as np
import pandas as pd
import datetime as dt
from scipy.stats import norm
from scipy import optimize
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def myfun_call(sigma):
    d1 = (np.log(S / K) + (r + sigma**2 / 2) * delta_t)/(sigma * np.sqrt(delta_t))
    d2 = d1 - sigma * np.sqrt(delta_t)
    c = S * norm.cdf(d1) - K * np.exp(-r * delta_t) * norm.cdf(d2)
    c = np.maximum(c, 0)
    return c - price_call

def myfun_put(sigma):
    d1 = (np.log(S / K) + (r + sigma**2 / 2) * delta_t)/(sigma * np.sqrt(delta_t))
    d2 = d1 - sigma * np.sqrt(delta_t)
    p = K * np.exp(-r * delta_t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    p = np.maximum(p, 0)
    return p - price_put


# 5月到期
S = 3.100
r = SHBOR_1M = 0.0142
delta_t = (dt.datetime(2026, 5, 27) - dt.datetime(2026, 5, 6)).days / 365
data = pd.read_excel('期权价格.xlsx', sheet_name='5月到期', header=0)
K_all_5 = data['行权价']
price_call_all = data['认购期权']
price_put_all = data['认沽期权']
sigma_0 = 0.3
sigma_call_5 = np.zeros(len(K_all_5))
sigma_put_5 = np.zeros(len(K_all_5))
for i in range(len(K_all_5)):
    K = K_all_5[i]
    price_call = price_call_all[i]
    # 找使 f(x)=0 的 x
    sigma_call_5[i] = optimize.fsolve(myfun_call, sigma_0).item()
    price_put = price_put_all[i]
    sigma_put_5[i] = optimize.fsolve(myfun_put, sigma_0).item()
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(K_all_5, sigma_call_5, 'bo-', label='看涨期权的隐含波动率', linewidth=2)
plt.plot(K_all_5, sigma_put_5, 'rs-', label='看跌期权的隐含波动率', linewidth=2)
plt.xlabel('行权价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('隐含波动率', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('5月份到期期权隐含波动率微笑', fontsize=24)
plt.grid()
plt.savefig('5月份到期期权隐含波动率微笑.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 6月到期
S = 3.100
r = SHBOR_1M = 0.0142
delta_t = (dt.datetime(2026, 6, 24) - dt.datetime(2026, 5, 6)).days / 365
data = pd.read_excel('期权价格.xlsx', sheet_name='6月到期', header=0)
K_all_5 = data['行权价']
price_call_all = data['认购期权']
price_put_all = data['认沽期权']
sigma_0 = 0.3
sigma_call_5 = np.zeros(len(K_all_5))
sigma_put_5 = np.zeros(len(K_all_5))
for i in range(len(K_all_5)):
    K = K_all_5[i]
    price_call = price_call_all[i]
    # 找使 f(x)=0 的 x
    sigma_call_5[i] = optimize.fsolve(myfun_call, sigma_0).item()
    price_put = price_put_all[i]
    sigma_put_5[i] = optimize.fsolve(myfun_put, sigma_0).item()
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(K_all_5, sigma_call_5, 'bo-', label='看涨期权的隐含波动率', linewidth=2)
plt.plot(K_all_5, sigma_put_5, 'rs-', label='看跌期权的隐含波动率', linewidth=2)
plt.xlabel('行权价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('隐含波动率', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('6月份到期期权隐含波动率微笑', fontsize=24)
plt.grid()
plt.savefig('6月份到期期权隐含波动率微笑.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 9月到期
S = 3.100
r = SHBOR_1M = 0.0142
delta_t = (dt.datetime(2026, 9, 23) - dt.datetime(2026, 5, 6)).days / 365
data = pd.read_excel('期权价格.xlsx', sheet_name='9月到期', header=0)
K_all_5 = data['行权价']
price_call_all = data['认购期权']
price_put_all = data['认沽期权']
sigma_0 = 0.3
sigma_call_5 = np.zeros(len(K_all_5))
sigma_put_5 = np.zeros(len(K_all_5))
for i in range(len(K_all_5)):
    K = K_all_5[i]
    price_call = price_call_all[i]
    # 找使 f(x)=0 的 x
    sigma_call_5[i] = optimize.fsolve(myfun_call, sigma_0).item()
    price_put = price_put_all[i]
    sigma_put_5[i] = optimize.fsolve(myfun_put, sigma_0).item()
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(K_all_5, sigma_call_5, 'bo-', label='看涨期权的隐含波动率', linewidth=2)
plt.plot(K_all_5, sigma_put_5, 'rs-', label='看跌期权的隐含波动率', linewidth=2)
plt.xlabel('行权价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('隐含波动率', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('9月份到期期权隐含波动率微笑', fontsize=24)
plt.grid()
plt.savefig('9月份到期期权隐含波动率微笑.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 12月到期
S = 3.100
r = SHBOR_1M = 0.0142
delta_t = (dt.datetime(2026, 12, 23) - dt.datetime(2026, 5, 6)).days / 365
data = pd.read_excel('期权价格.xlsx', sheet_name='12月到期', header=0)
K_all_5 = data['行权价']
price_call_all = data['认购期权']
price_put_all = data['认沽期权']
sigma_0 = 0.3
sigma_call_5 = np.zeros(len(K_all_5))
sigma_put_5 = np.zeros(len(K_all_5))
for i in range(len(K_all_5)):
    K = K_all_5[i]
    price_call = price_call_all[i]
    # 找使 f(x)=0 的 x
    sigma_call_5[i] = optimize.fsolve(myfun_call, sigma_0).item()
    price_put = price_put_all[i]
    sigma_put_5[i] = optimize.fsolve(myfun_put, sigma_0).item()
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(K_all_5, sigma_call_5, 'bo-', label='看涨期权的隐含波动率', linewidth=2)
plt.plot(K_all_5, sigma_put_5, 'rs-', label='看跌期权的隐含波动率', linewidth=2)
plt.xlabel('行权价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('隐含波动率', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('12月份到期期权隐含波动率微笑', fontsize=24)
plt.grid()
plt.savefig('12月份到期期权隐含波动率微笑.jpg', dpi=300, bbox_inches='tight')
plt.show()
