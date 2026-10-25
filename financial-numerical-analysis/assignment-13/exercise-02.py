# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})
plt.rcParams['font.family'] = 'SimHei'

# 数据整理
data_11_15 = pd.read_excel('RESSET_DRESSTK_2011_2015_1.xlsx')
data_11_15.columns = ['date', 'close']
data_11_15['date'] = pd.to_datetime(data_11_15['date'], format='%Y-%m-%d')
print(data_11_15)

data_16_20 = pd.read_excel('RESSET_DRESSTK_2016_2020_1.xlsx')
data_16_20.columns = ['date', 'close']
data_16_20['date'] = pd.to_datetime(data_16_20['date'], format='%Y-%m-%d')
print(data_16_20)

data_21_25 = pd.read_excel('RESSET_DRESSTK_2021__1.xlsx')
data_21_25.columns = ['date', 'close']
data_21_25['date'] = pd.to_datetime(data_21_25['date'], format='%Y-%m-%d')
print(data_21_25)

data = pd.concat([data_11_15, data_16_20, data_21_25], axis=0).reset_index(drop=True)
data = data[(data['date'] >= pd.to_datetime('2015-01-01', format='%Y-%m-%d'))
            &(data['date'] <= pd.to_datetime('2024-12-31', format='%Y-%m-%d'))].copy()
print(data)

print(data.isnull().sum())
data = data.fillna(method='ffill')

data['ln_close'] = np.log(data['close'])
print(data)

print(data.isnull().sum())

# data['delta_t'] = data['date'].diff().dt.days/365
# print(data)
#
# data['delta_t_sqrt'] = np.sqrt(data['delta_t'])
# print(data)

# 参数估计
data_annual_head = data.groupby(data['date'].dt.year).head(1)
print(data_annual_head)
data_annual_tail = data.groupby(data['date'].dt.year).tail(1)
print(data_annual_tail)

yield_annual = []
for i in range(10):
    yield_annual.append(data_annual_tail.iloc[i, 2]-data_annual_head.iloc[i, 2])
print(yield_annual)

mu = np.mean(yield_annual)
print(mu)

data['var_daily'] = data['ln_close'].diff()**2
print(data)
data['year'] = data['date'].dt.year
print(data)
var_annual = data.groupby('year')['var_daily'].sum()
print(var_annual)

sigma = np.sqrt(var_annual).mean()
print(sigma)

print('mu=', mu)
print('sigma=', sigma)

# 走势模拟
data_21_25 = data_21_25.set_index('date')
print(data_21_25)
sim_start_0 = data_21_25.loc['2025-01-02', 'close']
sim_start_1 = data_21_25.loc['2025-01-03', 'close']
print(sim_start_0, sim_start_1)

data_sim = pd.DataFrame({'date': pd.bdate_range('2025-01-01', '2025-12-31')})
print(data_sim)
print(len(data_sim))

sim = [sim_start_0]
pt = sim_start_0
for i in range(len(data_sim)-1):
    epsilon = np.random.normal(0, 1)
    pt += pt*(mu/len(data_sim)+sigma*epsilon*np.sqrt(1/len(data_sim)))
    sim.append(pt)
print(sim)

data_sim['sim'] = sim
print(data_sim)

# 画图输出
data_21_25 = pd.read_excel('RESSET_DRESSTK_2021__1.xlsx')
data_21_25.columns = ['date', 'real']
data_21_25['date'] = pd.to_datetime(data_21_25['date'], format='%Y-%m-%d')
data_real = data_21_25[(data_21_25['date'] >= pd.to_datetime('2025-01-01', format='%Y-%m-%d'))]

plt.figure(1, figsize=(14, 6))
plt.plot(data['date'], data['close'])
plt.plot(data_real['date'], data_real['real'])
plt.plot(data_sim['date'], sim)
plt.title('几何布朗运动模拟(600621)')
plt.legend(["2015-2024真实股价", '2025真实股价', '2025模拟股价'])

plt.savefig('homework13_2.jpg', dpi=300, bbox_inches='tight')
plt.show()


data_output = pd.merge(data_real, data_sim)
data_output['error'] = data_output['real'] - data_output['sim']
data_output['ratio'] = data_output['error']/data_output['error'].shift(1)

print(data_output)
print(f"{'simulate':<18}\t{'real':<18}\t{'Error':<18}\t{'Ratio':<18}")
for i in range(len(data_output['date'])):
    print(f"{data_output.loc[i, 'sim']:<18}\t{data_output.loc[i, 'real']:<18}\t{data_output.loc[i, 'error']:<18}\t{data_output.loc[i, 'ratio']:<18}")

# 解题过程中并没有充分使用差分，具体的改进方法有待后续的学习。
