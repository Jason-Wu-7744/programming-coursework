import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 定义期权B-S公式函数
def BSM_Model(S, K, sigma, r, dt):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * dt) / (sigma * np.sqrt(dt))
    d2 = d1 - sigma * np.sqrt(dt)

    price_call = S * norm.cdf(d1) - K * np.exp(-r * dt) * norm.cdf(d2)
    price_call = np.maximum(price_call, 0)

    price_put = K * np.exp(-r * dt) * norm.cdf(-d2) - S * norm.cdf(-d1)
    price_put = np.maximum(price_put, 0)

    return price_call, price_put

S = 3.024
K = 3.1
sigma = 0.1495
r = 0.01652
delta_t = 0.1562

# 标的资产现货价格变动
S_list = np.linspace(2.5, 3.5, 21)

price_call, price_put = BSM_Model(S_list, K, sigma, r, delta_t)
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(S_list, price_call, 'bo-', markersize=4, label='看涨期权', linewidth=2)
plt.plot(S_list, price_put, 'rs-', markersize=4, label='看跌期权', linewidth=2)
plt.xlabel('标的资产价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('期权价格', fontsize=18)
plt.yticks(fontsize=10)
# loc=0自动调整位置
plt.legend(loc=0, fontsize=18)
plt.title('期权价格与标的资产价格的关系', fontsize=24)
# 在图表背景上加网格线
plt.grid()
plt.savefig('期权价格与标的资产价格的关系.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 行权价格变动
K_list = np.linspace(2.5, 3.5, 21)

price_call, price_put = BSM_Model(S, K_list, sigma, r, delta_t)
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(K_list, price_call, 'bo-', markersize=4, label='看涨期权', linewidth=2)
plt.plot(K_list, price_put, 'rs-', markersize=4, label='看跌期权', linewidth=2)
plt.xlabel('行权价格', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('期权价格', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('期权价格与行权价格的关系', fontsize=24)
plt.grid()
plt.savefig('期权价格与行权价格的关系.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 波动率变动
sigma_list = np.linspace(0.1, 0.6, 21)

price_call, price_put = BSM_Model(S, K, sigma_list, r, delta_t)
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(sigma_list, price_call, 'bo-', markersize=4, label='看涨期权', linewidth=2)
plt.plot(sigma_list, price_put, 'rs-', markersize=4, label='看跌期权', linewidth=2)
plt.xlabel('波动率', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('期权价格', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('期权价格与波动率的关系', fontsize=24)
plt.grid()
plt.savefig('期权价格与波动率的关系.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 无风险利率
r_list = np.linspace(0.01, 0.1, 21)

price_call, price_put = BSM_Model(S, K, sigma, r_list, delta_t)
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(r_list, price_call, 'bo-', markersize=4, label='看涨期权', linewidth=2)
plt.plot(r_list, price_put, 'rs-', markersize=4, label='看跌期权', linewidth=2)
plt.xlabel('无风险利率', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('期权价格', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('期权价格与无风险利率的关系', fontsize=24)
plt.grid()
plt.savefig('期权价格与无风险利率的关系.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 到期期限
delta_t_list = np.linspace(0.01, 0.5, 21)

price_call, price_put = BSM_Model(S, K, sigma, r, delta_t_list)
plt.figure(figsize=(16, 9), dpi=200)
plt.plot(delta_t_list, price_call, 'bo-', markersize=4, label='看涨期权', linewidth=2)
plt.plot(delta_t_list, price_put, 'rs-', markersize=4, label='看跌期权', linewidth=2)
plt.xlabel('到期期限', fontsize=18)
plt.xticks(fontsize=10)
plt.ylabel('期权价格', fontsize=18)
plt.yticks(fontsize=10)
plt.legend(loc=0, fontsize=18)
plt.title('期权价格与到期期限的关系', fontsize=24)
plt.grid()
plt.savefig('期权价格与到期期限的关系.jpg', dpi=300, bbox_inches='tight')
plt.show()