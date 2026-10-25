import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model
from statsmodels.stats.diagnostic import het_arch
plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'


data_000001 = pd.read_excel("stock_data_2000_2020_v2.xlsx", sheet_name="上证综指")
data_000001.columns = ['date', 'close']
data_000001['date'] = pd.to_datetime(data_000001['date'])
plt.figure(1, figsize=(16, 9))
plt.title("2000-2020上证综指收盘价", fontsize=24)
plt.plot(data_000001['date'], data_000001['close'], lw=2)
plt.xlabel("时间")
plt.ylabel("股价")
plt.savefig('2000-2020上证综指收盘价.jpg', dpi=300, bbox_inches='tight')
# plt.show()

data_399001 = pd.read_excel("stock_data_2000_2020_v2.xlsx", sheet_name="深证成指")
data_399001.columns = ['date', 'close']
data_399001['date'] = pd.to_datetime(data_399001['date'])
plt.figure(2, figsize=(16, 9))
plt.title("2000-2020深证成指收盘价", fontsize=24)
plt.plot(data_399001['date'], data_399001['close'], lw=2)
plt.xlabel("时间")
plt.ylabel("股价")
plt.savefig('2000-2020深证成指收盘价.jpg', dpi=300, bbox_inches='tight')
# plt.show()

data_000858 = pd.read_csv("data_000858.csv")
data_000858['date'] = pd.to_datetime(data_000858['date'])
plt.figure(3, figsize=(16, 9))
plt.title("2000-2020五粮液收盘价", fontsize=24)
plt.plot(data_000858['date'], data_000858['close'], lw=2)
plt.xlabel("时间")
plt.ylabel("股价")
plt.savefig('2000-2020五粮液收盘价.jpg', dpi=300, bbox_inches='tight')
# plt.show()

data_600000 = pd.read_csv("data_600000.csv")
data_600000['date'] = pd.to_datetime(data_600000['date'])
plt.figure(4, figsize=(16, 9))
plt.title("2000-2020浦发银行收盘价", fontsize=24)
plt.plot(data_600000['date'], data_600000['close'], lw=2)
plt.xlabel("时间")
plt.ylabel("股价")
plt.savefig('2000-2020浦发银行收盘价.jpg', dpi=300, bbox_inches='tight')
# plt.show()
# 以上找的都是收盘价，应当取出异常值。如果更加细致严谨，应该使用复权价。

# 定义描述性统计函数
def descriptive_stats(returns):
    s = pd.Series(returns)
    stats = {
        '交易日天数': len(s),
        '均值': s.mean(),
        '标准差': s.std(),
        '偏度': s.skew(),
        '峰度': s.kurt()+3,
        '最大值': s.max(),
        '最小值': s.min(),
    }

    # 多阶自相关系数
    for lag in [1, 5, 10, 20]:
        # s.autocorr(lag=1)把序列向后平移1期
        stats[f'自相关系数(lag={lag})'] = s.autocorr(lag=lag)

    return pd.Series(stats)


# 从浦发银行开始
data = data_000858
p = data['close'].values
r = np.log(p[1:]) - np.log(p[:-1])
# 清理：只保留有限值（finite）
r = r[np.isfinite(r)]
# 去除因为分红、拆股导致的异常值
r = r[(r > -0.1) & (r < 0.1)]
print("浦发银行收益率的描述性统计")
print(descriptive_stats(r))
print("浦发银行收益率绝对值的描述性统计")
print(descriptive_stats(np.abs(r)))
# 指数收益率左偏，因为上涨慢
# 指数峰度>3，因为尖峰胖尾，中间收益率比较多

# 用ARCH-LM检验看有无ARCH条件异方差性
# Engle's ARCH-LM 检验
lm_stat, pvalue_lm, f_stat, pvalue_f = het_arch(r, maxlag=5)
print(f"LM统计量={lm_stat:.4f}, p值={pvalue_lm:.4f}")

# 用ARCH(1)估计
am_arch = arch_model(r*100, mean='constant', vol='arch', p=1, dist='normal')
res_arch = am_arch.fit()
print(res_arch.summary())
# 检验ARCH模型有效性，用标准化残差的 ARCH-LM 检验
# 提取标准化残差 z_t = ε_t / σ_t
std_resid_arch = res_arch.resid / res_arch.conditional_volatility
lm_stat, pvalue_lm, f_stat, pvalue_f = het_arch(std_resid_arch, maxlag=5)
print(f"LM统计量={lm_stat:.4f}, p值={pvalue_lm:.4f}")

# 用GARCH(1, 1)估计
am_garch = arch_model(r*100, mean='constant', vol='garch', p=1, q=1, dist='normal')
res_garch = am_garch.fit()
print(res_garch.summary())
# 检验GARCH模型有效性，用标准化残差的ARCH-LM检验
# 提取标准化残差 z_t = ε_t / σ_t
std_resid_arch = res_garch.resid / res_garch.conditional_volatility
lm_stat, pvalue_lm, f_stat, pvalue_f = het_arch(std_resid_arch, maxlag=5)
print(f"LM统计量={lm_stat:.4f}, p值={pvalue_lm:.4f}")

# 用EGARCH(1, 1)估计
am_egarch = arch_model(r*100, mean='constant', vol='egarch', p=1, o=1, q=1, dist='normal')
res_egarch = am_egarch.fit()
print(res_egarch.summary())
# 检验EGARCH模型有效性，用标准化残差的ARCH-LM检验
# 提取标准化残差 z_t = ε_t / σ_t
std_resid_arch = res_egarch.resid / res_egarch.conditional_volatility
lm_stat, pvalue_lm, f_stat, pvalue_f = het_arch(std_resid_arch, maxlag=5)
print(f"LM统计量={lm_stat:.4f}, p值={pvalue_lm:.4f}")

# 开始模拟浦发银行收益率
# 模拟ARCH(1)
sim_arch = arch_model(None, mean='constant', vol='arch', p=1, dist='normal')
sim_arch_data = sim_arch.simulate(res_arch.params, len(r))
print(sim_arch_data)
plt.figure(5, figsize=(16, 9))
plt.title("浦发银行波动率-模拟ARCH(1)模型", fontsize=24)
plt.xlabel("模拟观测序号")
plt.ylabel("条件波动率/模拟收益率（%）")
plt.plot(sim_arch_data['data'], color='green', lw=1.2, label='模拟收益率')
plt.plot(sim_arch_data['volatility'], color='orange', lw=2, label='条件波动率')
# 真实收益率同样需要*100
plt.plot(r*100, lw=1, label='真实收益率')
plt.legend(fontsize=16)
plt.savefig('浦发银行波动率-模拟ARCH(1)模型.jpg', dpi=300, bbox_inches='tight')
# 绿色是模拟收益率，黄色是条件波动率
# plt.show()

# 模拟GARCH(1, 1)
sim_garch = arch_model(None, mean='constant', vol='garch', p=1, q=1, dist='normal')
sim_garch_data = sim_garch.simulate(res_garch.params, len(r))
print(sim_garch_data)
plt.figure(6, figsize=(16, 9))
plt.title("浦发银行波动率-模拟GARCH(1, 1)模型", fontsize=24)
plt.xlabel("模拟观测序号")
plt.ylabel("条件波动率/模拟收益率（%）")
plt.plot(sim_garch_data['data'], color='green', lw=1.2, label='模拟收益率')
plt.plot(sim_garch_data['volatility'], color='orange', lw=2, label='条件波动率')
plt.plot(r*100, lw=1, label='真实收益率')
plt.legend(fontsize=16)
plt.savefig('浦发银行波动率-模拟GARCH(1, 1)模型.jpg', dpi=300, bbox_inches='tight')
# 绿色是模拟收益率，黄色是条件波动率
# plt.show()

# 模拟EGARCH(1, 1)
sim_egarch = arch_model(None, mean='constant', vol='egarch', p=1, o=1, q=1, dist='normal')
sim_egarch_data = sim_egarch.simulate(res_egarch.params, len(r))
print(sim_egarch_data)
plt.figure(7, figsize=(16, 9))
plt.title("浦发银行波动率-模拟EGARCH(1, 1)模型", fontsize=24)
plt.xlabel("模拟观测序号")
plt.ylabel("条件波动率/模拟收益率（%）")
plt.plot(sim_egarch_data['data'], color='green', lw=1.2, label='模拟收益率')
plt.plot(sim_egarch_data['volatility'], color='orange', lw=2, label='条件波动率')
plt.plot(r*100, lw=1, label='真实收益率')
plt.legend(fontsize=16)
plt.savefig('浦发银行波动率-模拟EGARCH(1, 1)模型.jpg', dpi=300, bbox_inches='tight')
# 绿色是模拟收益率，黄色是条件波动率
# plt.show()



