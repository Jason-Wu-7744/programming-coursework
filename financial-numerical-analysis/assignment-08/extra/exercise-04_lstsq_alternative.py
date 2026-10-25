# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
# Exp08_LPPLS_fit.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "STIXGeneral",
                     "font.size": 14,
                     "mathtext.fontset": "cm"})

# 1. 读数据 ----------------------------------------------------------
data = pd.read_csv('Exp08-Python-实验数据-LPPLS模型估参.csv', encoding='GB2312')
data.columns = ['time', 'close']
data['time'] = pd.to_datetime(data['time'], format='%Y/%m/%d')

# 2. 基准时间 & 相对时间 ----------------------------------------------
t0 = pd.to_datetime('2016-01-01')
tc = pd.to_datetime('2016-10-25')
tc_day = (tc - t0) / np.timedelta64(1, 'D')          # 298.0

data['t'] = (data['time'] - t0) / np.timedelta64(1, 'D')   # 交易日 -> 0,1,2,…
data['tau'] = tc_day - data['t']                           # tau = tc - t

# 3. 已知参数 ---------------------------------------------------------
m   = 0.2932
w   = 6.1023

# 4. 构造 3 个回归自变量 ----------------------------------------------
data['phi1'] = data['tau'] ** m
data['phi2'] = data['phi1'] * np.cos(w * np.log(data['tau']))
data['phi3'] = data['phi1'] * np.sin(w * np.log(data['tau']))

# 5. 线性回归 y = A + B*phi1 + C1*phi2 + C2*phi3 ----------------------
X = data[['phi1', 'phi2', 'phi3']].values
X = np.column_stack([np.ones(X.shape[0]), X])      # 加截距列
y = np.log(data['close']).values

beta, *_ = np.linalg.lstsq(X, y, rcond=None)        # beta = [A, B, C1, C2]
A, B, C1, C2 = beta
print('A =', A)
print('B =', B)
print('C1 =', C1)
print('C2 =', C2)

# 6. 回代拟合值 -------------------------------------------------------
data['lnp_fit'] = X @ beta
data['p_fit']   = np.exp(data['lnp_fit'])

# 7. 画图 -------------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(data['time'], data['close'], 'k.', label='实际收盘价')
plt.plot(data['time'], data['p_fit'], 'r-', lw=2, label='LPPLS 拟合')
plt.axvline(tc, ls='--', color='gray', label='tc = 2016-10-25')
plt.legend()
plt.title('LPPLS 线性系数拟合结果')
plt.ylabel('价格')
plt.tight_layout()
plt.show()