import numpy as np
import pandas as pd

# data = pd.read_excel('RESSET_MRESSTK_1.xlsx')
# # 用循环读数据
# for i in range(2, 11):
#     data_read = pd.read_excel('RESSET_MRESSTK_' + str(i) + '.xlsx')
#     data = pd.concat((data, data_read), axis=0, ignore_index=True)
#     del data_read
#
# print(data)
# data.columns = ['code', 'date', 'price']
# data.to_csv("data.csv", index=False)

data = pd.read_csv("data.csv")
data['date'] = pd.to_datetime(data['date'])
print(data)


class FastMomentumTest:
    """
    高速版动量/反转效应检验 - 向量化优化
    适合全A股2001-2025年大数据量
    """

    def __init__(self, data, N_list=[1, 3, 6, 12], M_list=[1, 3, 6, 12], n_portfolios=5):
        self.raw_data = data.copy()
        self.N_list = N_list
        self.M_list = M_list
        self.n_portfolios = n_portfolios
        self.ret_wide = None  # 宽格式收益率表

    def prepare_data(self):
        """关键优化：构建股票×时间的宽表，便于向量化计算"""
        df = self.raw_data.copy()
        df['date'] = pd.to_datetime(df['date'])

        # 按月聚合（防止同一月多个交易日）
        df['ym'] = df['date'].dt.to_period('M')
        monthly = df.groupby(['code', 'ym'])['price'].last().reset_index()

        # 计算月度收益率
        monthly['monret'] = monthly.groupby('code')['price'].pct_change()
        monthly = monthly.dropna()

        # 转为宽表：行=股票，列=月份
        self.ret_wide = monthly.pivot(index='code', columns='ym', values='monret')
        self.periods = self.ret_wide.columns.tolist()

        print(f"数据准备完成：{len(self.ret_wide)}只股票，{len(self.periods)}个月")
        return self.ret_wide

    def run_test(self):
        """核心计算逻辑 - 完全向量化"""
        if self.ret_wide is None:
            self.prepare_data()

        T = len(self.periods)
        results = {}

        for N in self.N_list:
            for M in self.M_list:
                print(f"计算 N={N}, M={M}...", end=" ")

                q_stats = [[] for _ in range(self.n_portfolios)]  # 存储收益率序列

                # 滑动窗口遍历（跳过前N个月，预留后M个月）
                for t in range(N, T - M):
                    # 过去N期数据
                    past_window = self.ret_wide.iloc[:, t - N:t]
                    # 未来M期数据
                    future_window = self.ret_wide.iloc[:, t:t + M]

                    # 向量化计算累积收益（忽略NaN）
                    past_cum = (1 + past_window).prod(axis=1, skipna=True) - 1
                    future_cum = (1 + future_window).prod(axis=1, skipna=True) - 1

                    # 筛选有效数据（两个窗口都有数据）
                    valid = past_cum.notna() & future_cum.notna()
                    if valid.sum() < 20:  # 至少20只股票才有效
                        continue

                    past_valid = past_cum[valid]
                    future_valid = future_cum[valid]

                    # 分组：按过去收益排序后等分
                    sorted_idx = past_valid.sort_values().index
                    group_size = len(sorted_idx) // self.n_portfolios

                    for g in range(self.n_portfolios):
                        start = g * group_size
                        end = len(sorted_idx) if g == self.n_portfolios - 1 else (g + 1) * group_size
                        group_codes = sorted_idx[start:end]

                        # 记录该组未来收益
                        group_ret = future_valid.loc[group_codes].mean()
                        q_stats[g].append(group_ret)

                # 计算统计量
                mean_rets = [np.mean(q) * 100 if len(q) > 0 else np.nan for q in q_stats]
                std_rets = [np.std(q) * 100 if len(q) > 0 else np.nan for q in q_stats]

                # 计算Q5-Q1的t统计量（判断显著性）
                if len(q_stats[0]) > 0 and len(q_stats[4]) > 0:
                    q5_q1_diff = np.array(q_stats[4]) - np.array(q_stats[0])
                    t_stat = np.mean(q5_q1_diff) / (np.std(q5_q1_diff) / np.sqrt(len(q5_q1_diff)))
                else:
                    t_stat = np.nan

                results[(N, M)] = {
                    'Q1': mean_rets[0], 'Q2': mean_rets[1], 'Q3': mean_rets[2],
                    'Q4': mean_rets[3], 'Q5': mean_rets[4],
                    'Q5-Q1': mean_rets[4] - mean_rets[0] if mean_rets[0] else np.nan,
                    't_stat': t_stat,
                    'n_obs': len(q_stats[0])
                }
                print(f"完成(n={len(q_stats[0])})")

        return results

    def print_results(self, results):
        """格式化输出"""
        print("\n" + "=" * 90)
        print("中国A股动量/反转效应检验结果 (2001-2025)")
        print("=" * 90)

        # 表头
        print(
            f"{'形成期N':<8} | {'持有期M':<8} | {'Q1(输家)':<10} | {'Q2':<10} | {'Q3':<10} | {'Q4':<10} | {'Q5(赢家)':<10} | {'Q5-Q1':<10} | {'t值':<8}")
        print("-" * 90)

        for N in self.N_list:
            for M in self.M_list:
                r = results[(N, M)]
                q5q1 = r['Q5-Q1']
                t_stat = r['t_stat']

                # 标记显著性
                sig = ""
                if abs(t_stat) > 2.58:
                    sig = "***"  # 1%显著
                elif abs(t_stat) > 1.96:
                    sig = "**"  # 5%显著
                elif abs(t_stat) > 1.64:
                    sig = "*"  # 10%显著

                effect = "动量" if q5q1 > 0 else "反转"

                print(f"{N:<8} | {M:<8} | {r['Q1']:>9.3f}% | {r['Q2']:>9.3f}% | {r['Q3']:>9.3f}% | "
                      f"{r['Q4']:>9.3f}% | {r['Q5']:>9.3f}% | {q5q1:>9.3f}% | {t_stat:>7.2f}{sig} | {effect}")

        print("=" * 90)
        print("注: ***, **, * 分别表示1%, 5%, 10%的显著性水平")
        print("    Q5-Q1 > 0 表示存在动量(惯性)效应")
        print("    Q5-Q1 < 0 表示存在反转效应")


# ================== 使用示例 ==================

test = FastMomentumTest(data, N_list=[1,3,6,12], M_list=[1,3,6,12])
results = test.run_test()
test.print_results(results)


# 结论：都是反转效应