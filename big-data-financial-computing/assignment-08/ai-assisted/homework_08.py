#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国股市尾部风险测度的估计与检验
——基于上海电力(600021)的VaR计算与评估
示例标的：上海电力 600021

实验内容：
  1. 获取上海电力日度收盘价数据，计算对数收益率
  2. 分别用RiskMetrics、Gamma-Normal(GARCH)、历史模拟法、POT方法计算VaR
  3. 样本内外数据量比为1/2，滚动窗口预测
  4. 利用Kupiec检验、Christoffersen检验和条件覆盖检验评估各种VaR方法
"""

import numpy as np
import pandas as pd
from scipy.stats import norm, chi2, genpareto, t as t_dist
import matplotlib.pyplot as plt
from arch import arch_model
import matplotlib
import warnings
warnings.filterwarnings('ignore')
matplotlib.rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'WenQuanYi Zen Hei', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.max_open_warning'] = 50

# ==================== 1. 数据读取与预处理 ====================
print("=" * 60)
print("步骤1：数据读取与预处理")
print("=" * 60)

# 从iFinD下载的上海电力(600021)日度数据读取
data = pd.read_csv('shdl_raw.csv')
# 按日期升序排列
data = data.sort_values('日期', ascending=True).reset_index(drop=True)
# 重命名列
data.columns = ['code', 'name', 'date', 'close']
data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')

# 计算对数收益率（百分比形式，乘以100）
data['return'] = np.log(data['close']) - np.log(data['close'].shift(periods=1))
data['return'] = data['return'] * 100

# 删除缺失值
data = data.dropna(subset=['return']).reset_index(drop=True)

print(f"数据范围：{data['date'].min().strftime('%Y-%m-%d')} 至 {data['date'].max().strftime('%Y-%m-%d')}")
print(f"有效交易日数：{len(data)}")
print(f"对数收益率统计：均值={data['return'].mean():.4f}%, 标准差={data['return'].std():.4f}%")

# 原始收盘价走势图
fig1, axes1 = plt.subplots(2, 1, figsize=(12, 8))
axes1[0].plot(data['date'], data['close'], linewidth=0.8)
axes1[0].set_title('上海电力(600021)日度收盘价走势', fontsize=14)
axes1[0].set_ylabel('收盘价（元）')
axes1[0].grid(True, alpha=0.3)

axes1[1].plot(data['date'], data['return'], linewidth=0.5)
axes1[1].set_title('上海电力(600021)日度对数收益率', fontsize=14)
axes1[1].set_ylabel('对数收益率（%）')
axes1[1].set_xlabel('日期')
axes1[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('fig1_price_return.png', dpi=150)
plt.close()
print("图1：收盘价与收益率走势图已保存 → fig1_price_return.png")

# ==================== 2. 样本划分 ====================
print("\n" + "=" * 60)
print("步骤2：样本划分（样本内外数据量比=1/2）")
print("=" * 60)

n = len(data)
n_sample_in = int(np.fix(n / 2))  # 样本内数据量：约1/2
# 根据作业要求，样本内外数据量比为1/2
# 前1/2数据作为样本内，后1/2用于滚动预测
l = np.fix(n / 2).astype(int)  # 初始样本内长度

r = data['return'].values  # 对数收益率序列（百分比）
dates = data['date'].values

print(f"总样本量：{n}")
print(f"初始样本内（估计窗口）长度 l = {l}")
print(f"滚动预测窗口次数 N = {n - l}")

# ==================== 3. RiskMetrics方法 ====================
print("\n" + "=" * 60)
print("步骤3：RiskMetrics方法计算VaR")
print("=" * 60)

VaR_RM = np.zeros(n)
qalpha_norm = norm.ppf(0.05)  # α=5%的标准正态分位数

for i in range(l, n):
    # 用前50个交易日的收益率估计正态分布参数
    mhat, shat = norm.fit(r[i-50:i])
    VaR_RM[i] = -(mhat + qalpha_norm * shat)

print(f"RiskMetrics VaR计算完成，预测次数：{np.sum(VaR_RM > 0)}")
print(f"VaR_RM 均值：{np.mean(VaR_RM[l:]):.4f}%")

# ==================== 4. Gamma-Normal (GARCH) 方法 ====================
print("\n" + "=" * 60)
print("步骤4：Gamma-Normal方法（AR(1)-GARCH(2,2)）计算VaR")
print("=" * 60)

VaR_GN = np.zeros(n)

for i in range(l, n):
    # 用前200个交易日的数据估计AR(1)-GARCH(2,2)模型
    try:
        am_ar_garch = arch_model(r[i-200:i], mean='AR', lags=1,
                                 vol='Garch', p=2, q=2, dist='normal')
        res_ar_garch = am_ar_garch.fit(disp='off')
        a = res_ar_garch.forecast(horizon=1, align='origin')
        mu = a.mean['h.1'].iloc[-1]
        sgm2 = a.variance['h.1'].iloc[-1]
        VaR_GN[i] = -(mu + qalpha_norm * np.sqrt(sgm2))
    except Exception:
        # 如果估计失败，使用前一个VaR值
        VaR_GN[i] = VaR_GN[i-1] if i > l else 0

print(f"Gamma-Normal VaR计算完成")
print(f"VaR_GN 均值：{np.mean(VaR_GN[l:]):.4f}%")

# ==================== 5. 历史模拟法 (Historical Simulation) ====================
print("\n" + "=" * 60)
print("步骤5：历史模拟法计算VaR（窗口=200）")
print("=" * 60)

VaR_HS = np.zeros(n)
window_HS = 200
qalpha_idx = int(window_HS * 0.05)  # 5%分位数对应的索引

for i in range(l, n):
    his_sample = r[i-window_HS:i]
    his_sample = np.sort(his_sample)
    VaR_HS[i] = -his_sample[qalpha_idx - 1]

print(f"历史模拟法 VaR计算完成")
print(f"VaR_HS 均值：{np.mean(VaR_HS[l:]):.4f}%")

# ==================== 6. POT方法 (Peaks Over Threshold) ====================
print("\n" + "=" * 60)
print("步骤6：POT方法（极值理论）计算VaR")
print("=" * 60)

VaR_EVT = np.zeros(n)
alpha = 0.05
window_EVT = 200

for i in range(l, n):
    his_sample = r[i-window_EVT:i]
    his_sample = np.sort(his_sample)
    ind = np.fix(len(his_sample) * 0.1).astype(int)
    evt_sample = np.abs(his_sample[:ind])  # 取最左尾（最负的收益率）
    u = np.abs(his_sample[ind])  # 阈值：样本的10%分位数
    exceed_values = evt_sample - u  # 超出部分
    n_total = len(his_sample)
    Nu = len(exceed_values)

    if Nu > 0 and np.std(exceed_values) > 1e-10:
        try:
            parmhat = genpareto.fit(exceed_values, floc=0)
            kHat = parmhat[0]      # 尾指数
            sigmaHat = parmhat[2]  # 尺度参数

            if abs(kHat) > 1e-8:
                VaR_EVT[i] = u + sigmaHat / kHat * ((alpha * n_total / Nu) ** (-kHat) - 1)
            else:
                # kHat ≈ 0，退化为指数分布
                VaR_EVT[i] = u + sigmaHat * np.log(Nu / (alpha * n_total))
        except Exception:
            VaR_EVT[i] = VaR_EVT[i-1] if i > l else 0
    else:
        VaR_EVT[i] = VaR_EVT[i-1] if i > l else 0

print(f"POT方法 VaR计算完成")
print(f"VaR_EVT 均值：{np.mean(VaR_EVT[l:]):.4f}%")

# ==================== 7. VaR预测结果可视化 ====================
print("\n" + "=" * 60)
print("步骤7：绘制VaR预测值时间序列图")
print("=" * 60)

# 只用预测期的数据
start_idx = l
r_pred = r[start_idx:]
dates_pred = dates[start_idx:]
VaR_RM_pred = VaR_RM[start_idx:]
VaR_GN_pred = VaR_GN[start_idx:]
VaR_HS_pred = VaR_HS[start_idx:]
VaR_EVT_pred = VaR_EVT[start_idx:]

fig2, axes2 = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

ax = axes2[0]
ax.plot(dates_pred, r_pred, linewidth=0.5, alpha=0.7, label='收益率')
ax.plot(dates_pred, -VaR_RM_pred, 'r-', linewidth=0.8, label='VaR_RiskMetrics')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylabel('收益率/VaR (%)')
ax.set_title('RiskMetrics方法 VaR预测', fontsize=12)
ax.grid(True, alpha=0.3)

ax = axes2[1]
ax.plot(dates_pred, r_pred, linewidth=0.5, alpha=0.7, label='收益率')
ax.plot(dates_pred, -VaR_GN_pred, 'b-', linewidth=0.8, label='VaR_GammaNormal')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylabel('收益率/VaR (%)')
ax.set_title('Gamma-Normal (GARCH)方法 VaR预测', fontsize=12)
ax.grid(True, alpha=0.3)

ax = axes2[2]
ax.plot(dates_pred, r_pred, linewidth=0.5, alpha=0.7, label='收益率')
ax.plot(dates_pred, -VaR_HS_pred, 'g-', linewidth=0.8, label='VaR_HistSim')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylabel('收益率/VaR (%)')
ax.set_title('历史模拟法 VaR预测 (窗口=200)', fontsize=12)
ax.grid(True, alpha=0.3)

ax = axes2[3]
ax.plot(dates_pred, r_pred, linewidth=0.5, alpha=0.7, label='收益率')
ax.plot(dates_pred, -VaR_EVT_pred, 'm-', linewidth=0.8, label='VaR_POT')
ax.legend(loc='upper right', fontsize=9)
ax.set_ylabel('收益率/VaR (%)')
ax.set_xlabel('日期')
ax.set_title('POT方法（极值理论） VaR预测', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fig2_VaR_predictions.png', dpi=150)
plt.close()
print("图2：四种VaR方法预测值时间序列图已保存 → fig2_VaR_predictions.png")

# 四种VaR预测值对比图
fig3, ax3 = plt.subplots(figsize=(14, 6))
ax3.plot(dates_pred, -VaR_RM_pred, 'r-', linewidth=0.8, alpha=0.8, label='RiskMetrics')
ax3.plot(dates_pred, -VaR_GN_pred, 'b-', linewidth=0.8, alpha=0.8, label='Gamma-Normal')
ax3.plot(dates_pred, -VaR_HS_pred, 'g-', linewidth=0.8, alpha=0.8, label='历史模拟法')
ax3.plot(dates_pred, -VaR_EVT_pred, 'm-', linewidth=0.8, alpha=0.8, label='POT')
ax3.set_title('四种VaR方法预测值对比（上海电力 600021）', fontsize=14)
ax3.set_ylabel('VaR (%)')
ax3.set_xlabel('日期')
ax3.legend(loc='upper right', fontsize=10)
ax3.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('fig3_VaR_comparison.png', dpi=150)
plt.close()
print("图3：四种VaR方法对比图已保存 → fig3_VaR_comparison.png")

# ==================== 8. 数据导出到Excel ====================
print("\n" + "=" * 60)
print("步骤8：导出预测结果到Excel")
print("=" * 60)

df_export = pd.DataFrame({
    'date': dates,
    'return': r,
    'VaR_RiskMetrics': VaR_RM,
    'VaR_GammaNormal': VaR_GN,
    'VaR_HistSim': VaR_HS,
    'VaR_POT': VaR_EVT
})
df_export.to_excel('Var_results_600021.xlsx', index=False)
print("预测结果已导出 → Var_results_600021.xlsx")

# ==================== 9. VaR回测检验 ====================
print("\n" + "=" * 60)
print("步骤9：VaR回测检验（Kupiec、Christoffersen、条件覆盖检验）")
print("=" * 60)


def myfun_Kupiec(r, VaR, pstar):
    """Kupiec检验（无条件覆盖检验）"""
    N = np.sum(r < -VaR)  # 实际损失超过VaR的天数
    T = len(r)
    if N == 0 or N == T:
        LRuc = np.nan
        pvalue_LRuc = np.nan
    else:
        LRuc = -2 * ((T - N) * np.log(1 - pstar) + N * np.log(pstar)) \
               + 2 * ((T - N) * np.log(1 - N / T) + N * np.log(N / T))
        pvalue_LRuc = 1 - chi2.cdf(LRuc, 1)
    return LRuc, pvalue_LRuc, N


def myfun_Christoffersen(r, VaR):
    """Christoffersen检验（独立性检验）"""
    ind = (r < -VaR).astype(int)
    ind1 = ind[:-1]
    ind2 = ind[1:]

    n00 = np.sum((ind1 == 0) & (ind2 == 0))
    n01 = np.sum((ind1 == 0) & (ind2 == 1))
    n10 = np.sum((ind1 == 1) & (ind2 == 0))
    n11 = np.sum((ind1 == 1) & (ind2 == 1))

    # 避免分母为零
    if (n01 + n00) == 0 or (n10 + n11) == 0:
        return np.nan, np.nan

    Pi01 = n01 / (n01 + n00)
    Pi11 = n11 / (n10 + n11)
    Pi2 = (n01 + n11) / (n00 + n01 + n10 + n11)

    LRind = (n00 + n10) * np.log(1 - Pi2) + (n01 + n11) * np.log(Pi2) \
            - n00 * np.log(1 - Pi01) - n01 * np.log(Pi01) \
            - n10 * np.log(1 - Pi11) - n11 * np.log(Pi11)
    LRind = LRind * (-2)
    pvalue_LRind = 1 - chi2.cdf(LRind, 1)
    return LRind, pvalue_LRind


def myfun_Kupiec_Christoffersen(LRuc, LRind):
    """条件覆盖检验（联合检验）"""
    LRcc = LRuc + LRind
    pvalue_LRcc = 1 - chi2.cdf(LRcc, 2)
    return LRcc, pvalue_LRcc


# 准备检验数据（仅预测期）
ind_pred = VaR_RM > 0  # 有效VaR预测
r_test = r[ind_pred]
VaR_RM_test = VaR_RM[ind_pred]
VaR_GN_test = VaR_GN[ind_pred]
VaR_HS_test = VaR_HS[ind_pred]
VaR_EVT_test = VaR_EVT[ind_pred]

pstar = 0.05
print(f"\n有效预测样本数：{len(r_test)}")
print(f"显著性水平 α = {pstar}")
print(f"\n{'方法':<16s} {'突破次数':>8s} {'突破率':>8s}")
for name, var in [('RiskMetrics', VaR_RM_test), ('Gamma-Normal', VaR_GN_test),
                  ('HistSim', VaR_HS_test), ('POT', VaR_EVT_test)]:
    n_breaks = np.sum(r_test < -var)
    rate = n_breaks / len(r_test) * 100
    print(f"{name:<16s} {n_breaks:>8d} {rate:>7.2f}%")

# 对各方法进行检验
methods = {
    'RiskMetrics': (VaR_RM_test, 'RiskMetrics'),
    'Gamma-Normal': (VaR_GN_test, 'Gamma-Normal(GARCH)'),
    'HistSim': (VaR_HS_test, '历史模拟法'),
    'POT': (VaR_EVT_test, 'POT(极值理论)')
}

results = {}
for key, (var, name) in methods.items():
    LRuc, pLRuc, N_breaks = myfun_Kupiec(r_test, var, pstar)
    LRind, pLRind = myfun_Christoffersen(r_test, var)
    LRcc, pLRcc = myfun_Kupiec_Christoffersen(LRuc, LRind)
    results[key] = {
        'name': name,
        'LRuc': LRuc, 'pLRuc': pLRuc,
        'LRind': LRind, 'pLRind': pLRind,
        'LRcc': LRcc, 'pLRcc': pLRcc,
        'N_breaks': N_breaks
    }

# 打印检验结果表格
print(f"\n{'':<16s} {'LRuc':>10s} {'pLRuc':>10s} "
      f"{'LRind':>10s} {'pLRind':>10s} {'LRcc':>10s} {'pLRcc':>10s}")
print("-" * 76)
for key, res in results.items():
    print(f"{res['name']:<16s} {res['LRuc']:>10.4f} {res['pLRuc']:>10.4f} "
          f"{res['LRind']:>10.4f} {res['pLRind']:>10.4f} "
          f"{res['LRcc']:>10.4f} {res['pLRcc']:>10.4f}")

# 保存检验结果到Excel
df_test = pd.DataFrame({
    '方法': [res['name'] for res in results.values()],
    '突破次数': [res['N_breaks'] for res in results.values()],
    'LRuc': [res['LRuc'] for res in results.values()],
    'pLRuc': [res['pLRuc'] for res in results.values()],
    'LRind': [res['LRind'] for res in results.values()],
    'pLRind': [res['pLRind'] for res in results.values()],
    'LRcc': [res['LRcc'] for res in results.values()],
    'pLRcc': [res['pLRcc'] for res in results.values()]
})
df_test.to_excel('Var_backtest_results_600021.xlsx', index=False)
print("\n回测检验结果已导出 → Var_backtest_results_600021.xlsx")

# ==================== 10. 收益率分布直方图与VaR标记 ====================
print("\n" + "=" * 60)
print("步骤10：绘制收益率分布与VaR对比图")
print("=" * 60)

fig4, axes4 = plt.subplots(2, 2, figsize=(12, 10))

for idx, (key, res) in enumerate(results.items()):
    ax = axes4[idx // 2][idx % 2]
    var_val = methods[key][0]
    ax.hist(r_test, bins=80, density=True, alpha=0.6, color='steelblue')
    ax.axvline(x=-np.mean(var_val), color='red', linestyle='--',
               linewidth=2, label=f'平均VaR={np.mean(var_val):.3f}%')
    # 叠加正态分布曲线
    x = np.linspace(r_test.min(), r_test.max(), 200)
    ax.plot(x, norm.pdf(x, r_test.mean(), r_test.std()), 'orange',
            linewidth=1.5, label='正态分布拟合')
    ax.set_title(f'{res["name"]}', fontsize=12)
    ax.set_xlabel('对数收益率 (%)')
    ax.set_ylabel('密度')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fig4_VaR_distribution.png', dpi=150)
plt.close()
print("图4：收益率分布与VaR对比图已保存 → fig4_VaR_distribution.png")

print("\n" + "=" * 60)
print("所有计算已完成！")
print("输出文件：")
print("  - fig1_price_return.png         : 收盘价与收益率走势图")
print("  - fig2_VaR_predictions.png      : 四种VaR方法预测值时间序列图")
print("  - fig3_VaR_comparison.png       : 四种VaR方法对比图")
print("  - fig4_VaR_distribution.png     : 收益率分布与VaR对比图")
print("  - Var_results_600021.xlsx        : VaR预测结果数据")
print("  - Var_backtest_results_600021.xlsx: 回测检验结果")
print("=" * 60)
