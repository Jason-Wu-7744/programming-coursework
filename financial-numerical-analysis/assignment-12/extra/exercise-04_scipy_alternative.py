# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import numpy as np
import pandas as pd
from scipy.stats import lognorm   # 只多引入这一行

# ---- 读数据 + MLE ----
data = pd.read_excel('Exp12-Python-实验数据-对数正态分布数据样本.xlsx')
data.columns = ['x']
mu = np.log(data['x']).mean()
sigma = np.log(data['x']).std(ddof=0)   # MLE 分母 n

# ---- 概率计算 ----
a = 5
p_exact = 1 - lognorm.cdf(a, s=sigma, scale=np.exp(mu))
print('P(X > 5) =', p_exact)