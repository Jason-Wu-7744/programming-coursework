import numpy as np
import pandas as pd
import datetime as dt

data_bonds = pd.read_excel('债券数据.xlsx')
data_bonds['到期日期'] = pd.to_datetime(data_bonds['到期日期'])
print(data_bonds)

# 定义函数
# 计算应计利息
def Accrued_Interest(Par_value, C_rate, T_now, T_previous, T_next, M):
    AI = Par_value * C_rate / M * (T_now - T_previous).days / (T_next - T_previous).days
    return AI

# 付息日的计算
def Tenor(T_now, T_next, T_maturity, M):
    tenor_next = (T_next - T_now).days / 365
    tenor_maturity = (T_maturity - T_now).days / 365
    N = int(tenor_maturity * M) + 1
    t_list = np.arange(N) / M + tenor_next
    return t_list

# 二分法算到期收益率
def YTM(a, b, Tenor, Cashflow, Price):
    '''
    参数a为到期收益率的下限
    参数b为到期收益率的上限
    '''

    def myfun(y):
        term = np.exp(-y * Tenor) * Cashflow
        return np.sum(term) - Price

    if myfun(a) * myfun(b) > 0:
        print('上下限选择错误')
        return None
    else:
        Epsilon = 1E-6
        while b - a > Epsilon:
            mid = (a + b) / 2
            if myfun(mid) == 0:
                rslt = mid
                return rslt
                break
            elif myfun(a) * myfun(mid) < 0:
                b = mid
            else:
                a = mid
        ytm = (a + b) / 2
        return ytm

# 用到期收益率算久期
def Duration(Tenor, Cashflow, Ytm):
    term = Cashflow * np.exp(-Ytm * Tenor)
    V = sum(term)                    # 原代码保持 sum(term)
    duration = np.sum(Tenor * term) / V
    return duration

# 当前已知条件
# 债券面值
par_value = 100
t_now = dt.datetime(2026, 4, 14)
# 定义全价、久期列表
Prices_full = []
Durations = []

# 开始计算第一支债券
i = 0
bond_name = data_bonds['证券简称'].iloc[i]
coupon_rate = data_bonds['票面利率'].iloc[i] / 100
m = data_bonds['每年付息次数'].iloc[i]
t_maturity = data_bonds['到期日期'].iloc[i].to_pydatetime()
price_bond_clearn = data_bonds['净价'].iloc[i]
print(bond_name, coupon_rate, m, t_maturity, price_bond_clearn)

# 应计利息
t_previous = dt.datetime(2026, 2, 3)
t_next = dt.datetime(2027, 2, 3)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
print('"%s"的应计利息为：%.4f元' % (bond_name, AI))

# 全价
price_bond_full = price_bond_clearn + AI
Prices_full.append(price_bond_full)
print('"%s"的全价为：%.4f元' % (bond_name, price_bond_full))

# 付息日序列（当前日期）
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)

# 现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)

# 到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=price_bond_full)
print('%s，“%s”的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))

# 套保结束日期 & 重新计算 tenor
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
# 计算到期收益率所用的现金流节点和计算久期所用的现金流节点不同，前者贴到现在套保开始日期，后者贴到一个月后的套保结束日期
t_next = dt.datetime(2027, 2, 3)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)

# 久期计算
duration_bond = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
Durations.append(duration_bond)
print('%s，“%s”的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, duration_bond))


# 开始计算第二支债券
i = 1
bond_name = data_bonds['证券简称'].iloc[i]
coupon_rate = data_bonds['票面利率'].iloc[i] / 100
m = data_bonds['每年付息次数'].iloc[i]
t_maturity = data_bonds['到期日期'].iloc[i].to_pydatetime()
price_bond_clearn = data_bonds['净价'].iloc[i]
print(bond_name, coupon_rate, m, t_maturity, price_bond_clearn)
# 应计利息
t_previous = dt.datetime(2025, 11, 3)
t_next = dt.datetime(2026, 5, 3)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
print('"%s"的应计利息为：%.4f元' % (bond_name, AI))
# 全价
price_bond_full = price_bond_clearn + AI
Prices_full.append(price_bond_full)
print('"%s"的全价为：%.4f元' % (bond_name, price_bond_full))
# 付息日序列（当前日期）
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
# 现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=price_bond_full)
print('%s，“%s”的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))
# 套保结束日期 & 重新计算 tenor
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
# 计算到期收益率所用的现金流节点和计算久期所用的现金流节点不同，前者贴到现在套保开始日期，后者贴到一个月后的套保结束日期
t_next = dt.datetime(2026, 11, 3)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 久期计算
duration_bond = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
Durations.append(duration_bond)
print('%s，“%s”的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, duration_bond))

# 开始计算第三支债券
i = 2
bond_name = data_bonds['证券简称'].iloc[i]
coupon_rate = data_bonds['票面利率'].iloc[i] / 100
m = data_bonds['每年付息次数'].iloc[i]
t_maturity = data_bonds['到期日期'].iloc[i].to_pydatetime()
price_bond_clearn = data_bonds['净价'].iloc[i]
print(bond_name, coupon_rate, m, t_maturity, price_bond_clearn)
# 应计利息
t_previous = dt.datetime(2025, 7, 6)
t_next = dt.datetime(2026, 7, 6)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
print('"%s"的应计利息为：%.4f元' % (bond_name, AI))
# 全价
price_bond_full = price_bond_clearn + AI
Prices_full.append(price_bond_full)
print('"%s"的全价为：%.4f元' % (bond_name, price_bond_full))
# 付息日序列（当前日期）
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
# 现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=price_bond_full)
print('%s，“%s”的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))
# 套保结束日期 & 重新计算 tenor
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
# 计算到期收益率所用的现金流节点和计算久期所用的现金流节点不同，前者贴到现在套保开始日期，后者贴到一个月后的套保结束日期
t_next = dt.datetime(2026, 7, 6)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 久期计算
duration_bond = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
Durations.append(duration_bond)
print('%s，“%s”的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, duration_bond))

# 开始计算第四支债券
i = 3
bond_name = data_bonds['证券简称'].iloc[i]
coupon_rate = data_bonds['票面利率'].iloc[i] / 100
m = data_bonds['每年付息次数'].iloc[i]
t_maturity = data_bonds['到期日期'].iloc[i].to_pydatetime()
price_bond_clearn = data_bonds['净价'].iloc[i]
print(bond_name, coupon_rate, m, t_maturity, price_bond_clearn)
# 应计利息
t_previous = dt.datetime(2026, 2, 9)
t_next = dt.datetime(2026, 8, 9)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
print('"%s"的应计利息为：%.4f元' % (bond_name, AI))
# 全价
price_bond_full = price_bond_clearn + AI
Prices_full.append(price_bond_full)
print('"%s"的全价为：%.4f元' % (bond_name, price_bond_full))
# 付息日序列（当前日期）
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
# 现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=price_bond_full)
print('%s，“%s”的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))
# 套保结束日期 & 重新计算 tenor
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
# 计算到期收益率所用的现金流节点和计算久期所用的现金流节点不同，前者贴到现在套保开始日期，后者贴到一个月后的套保结束日期
t_next = dt.datetime(2026, 8, 9)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 久期计算
duration_bond = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
Durations.append(duration_bond)
print('%s，“%s”的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, duration_bond))

# 开始计算第五支债券
i = 6
bond_name = data_bonds['证券简称'].iloc[i]
coupon_rate = data_bonds['票面利率'].iloc[i] / 100
m = data_bonds['每年付息次数'].iloc[i]
t_maturity = data_bonds['到期日期'].iloc[i].to_pydatetime()
price_bond_clearn = data_bonds['净价'].iloc[i]
print(bond_name, coupon_rate, m, t_maturity, price_bond_clearn)
# 应计利息
t_previous = dt.datetime(2025, 12, 4)
t_next = dt.datetime(2026, 6, 4)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
print('"%s"的应计利息为：%.4f元' % (bond_name, AI))
# 全价
price_bond_full = price_bond_clearn + AI
Prices_full.append(price_bond_full)
print('"%s"的全价为：%.4f元' % (bond_name, price_bond_full))
# 付息日序列（当前日期）
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
# 现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=price_bond_full)
print('%s，“%s”的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))
# 套保结束日期 & 重新计算 tenor
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
# 计算到期收益率所用的现金流节点和计算久期所用的现金流节点不同，前者贴到现在套保开始日期，后者贴到一个月后的套保结束日期
t_next = dt.datetime(2026, 6, 4)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
print(tenor)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
print(cashflow)
# 久期计算
duration_bond = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
Durations.append(duration_bond)
print('%s，“%s”的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, duration_bond))


# 选取CTD券
bond_name = '25附息国债25'
m = 1
t_maturity = dt.datetime(2032, 12, 25)
coupon_rate = 0.0166
price_bond_clearn = 100.0695
# CTD应计利息
t_previous = dt.datetime(2025, 12, 25)
t_next = dt.datetime(2026, 12, 25)
AI = Accrued_Interest(Par_value=par_value,
                      C_rate=coupon_rate,
                      T_now=t_now,
                      T_previous=t_previous,
                      T_next=t_next,
                      M=m)
# CTD全价
price_bond_full_CTD = price_bond_clearn + AI
Price_full_CTD = price_bond_full_CTD
# CTD付息日序列
tenor = Tenor(T_now=t_now,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
# CTD现金流
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
# CTD到期收益率
ytm = YTM(a=0.01, b=0.1, Tenor=tenor, Cashflow=cashflow, Price=Price_full_CTD)
print('%s，CTD券"%s"的到期收益率（连续复利）为：%.4f%%' % (t_now.strftime('%Y-%m-%d'), bond_name, ytm * 100))
# CTD久期
t_settle = dt.datetime(2026, 5, 14)     # 套保结束日期
t_next = dt.datetime(2026, 12, 25)
tenor = Tenor(T_now=t_settle,
              T_next=t_next,
              T_maturity=t_maturity,
              M=m)
cashflow = np.ones_like(tenor) * par_value * coupon_rate / m
cashflow[-1] = cashflow[-1] + par_value
Duration_CTD = Duration(Tenor=tenor, Cashflow=cashflow, Ytm=ytm)
print('%s，CTD券"%s"的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), bond_name, Duration_CTD))
print(Price_full_CTD)

# 构造债券投资组合
s = 1e5
Prices_full = np.array(Prices_full)
V_H = np.sum(s * Prices_full)
print('%s，债券投资组合的总金额为：%.4f' % (t_now.strftime('%Y-%m-%d'), V_H))

# 债券投资组合久期的计算
w = Prices_full / Prices_full.sum()
print(w)
print('-'*30)
Durations = np.array(Durations)
D_H = np.sum(w * Durations)
print('%s，债券投资组合的久期为：%.4f' % (t_settle.strftime('%Y-%m-%d'), D_H))

# 国债期货套期保值比例
D_G = Duration_CTD
price_futures = 108.505
futures_multiplier = 10000
V_G = price_futures * futures_multiplier

# 久期法套保比率：N = (D_H × V_H) / (D_G × V_G)
N = D_H * V_H / (D_G * V_G)

print('运用国债期货T2606进行套期保值时，应该卖出期货的数量为：%d份' % round(N))

print(Prices_full)
print(Durations)