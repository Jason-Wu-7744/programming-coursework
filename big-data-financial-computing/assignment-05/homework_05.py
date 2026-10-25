import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})
plt.rcParams['font.family'] = 'SimHei'
plt.figure(1, figsize=(14, 6))

data_rf = pd.read_excel("RESSET_MRESSTK_1.xlsx")
data_rf.columns = ['date', 'rf']
data_rf['date'] = pd.to_datetime(data_rf['date'])
print(data_rf)

# 读取三因子数据，使用流通市值
data_ff = pd.read_excel("RESSET_THRFACDAT_MONTHLY_1.xlsx")
data_ff = data_ff[(data_ff['交易所标识_Exchflg'] == 0) &
                  (data_ff['市场标识_Mktflg'] == 'A')]
data_ff = data_ff.iloc[:, -4:]
data_ff.columns = ['date', 'Rm', 'SMB', 'HML']
data_ff['date'] = pd.to_datetime(data_ff['date'])
print(data_ff)
print(data_ff.columns)


data = pd.read_excel("RESSET_IDXCSIMONRET_1.xlsx")
# print(data)
data['交易日期_TrdDt'] = pd.to_datetime(data['交易日期_TrdDt'])
data = data.pivot(index='交易日期_TrdDt',
                  columns='指数名称_IdxNm',
                  values='收盘价_ClPr').reset_index()
print(data)
# print(data.columns)

p1 = data.iloc[:, 2].values
p2 = data.iloc[:, 3].values
p3 = data.iloc[:, 4].values
p4 = data.iloc[:, 5].values
p5 = data.iloc[:, 6].values
p6 = data.iloc[:, 7].values
p7 = data.iloc[:, 8].values
p8 = data.iloc[:, 9].values
p9 = data.iloc[:, 10].values
p10 = data.iloc[:, 11].values
# data['rf'] = data_rf['rf']
pmkt = data.iloc[:, 1].values
# data['Rm'] = data_ff['Rm']
# data['SMB'] = data_ff['SMB']
# data['HML'] = data_ff['HML']

data_cov = pd.DataFrame({"date": data_ff['date'][1:]}).reset_index()
data_cov['Rm'] = data_ff['Rm'].values[1:]
data_cov['SMB'] = data_ff['SMB'].values[1:]
data_cov['HML'] = data_ff['HML'].values[1:]
data_cov['rf'] = data_rf['rf'].values[1:]
data_cov['rm'] = np.log(pmkt[1:]) - np.log(pmkt[:-1])
data_cov = data_cov.ffill()
data_cov['r1'] = np.log(p1[1:]) - np.log(p1[:-1]) - data_cov['rf']
data_cov['r2'] = np.log(p2[1:]) - np.log(p2[:-1]) - data_cov['rf']
data_cov['r3'] = np.log(p3[1:]) - np.log(p3[:-1]) - data_cov['rf']
data_cov['r4'] = np.log(p4[1:]) - np.log(p4[:-1]) - data_cov['rf']
data_cov['r5'] = np.log(p5[1:]) - np.log(p5[:-1]) - data_cov['rf']
data_cov['r6'] = np.log(p6[1:]) - np.log(p6[:-1]) - data_cov['rf']
data_cov['r7'] = np.log(p7[1:]) - np.log(p7[:-1]) - data_cov['rf']
data_cov['r8'] = np.log(p8[1:]) - np.log(p8[:-1]) - data_cov['rf']
data_cov['r9'] = np.log(p9[1:]) - np.log(p9[:-1]) - data_cov['rf']
data_cov['r10'] = np.log(p10[1:]) - np.log(p10[:-1]) - data_cov['rf']
# print(data_cov.columns)
# 从 data_cov 中分别提取「日期列」和「10个行业的超额收益列」，然后重新拼成一个新的 DataFrame
data_cov_1 = data_cov.iloc[:, 1].reset_index()
data_cov_2 = data_cov.iloc[:, 7:].reset_index()
data_cov = pd.concat([data_cov_1, data_cov_2], axis=1)
print("-------------------------------")
print(data_cov)
data_cov['Rm'] = data_ff['Rm'].values[1:]
data_cov['SMB'] = data_ff['SMB'].values[1:]
data_cov['HML'] = data_ff['HML'].values[1:]
data_cov['rf'] = data_rf['rf'].values[1:]
data_cov['rm'] = np.log(pmkt[1:]) - np.log(pmkt[:-1])
data_cov = data_cov.ffill()
data_cov = data_cov.iloc[:, 1:]
data_cov_1 = data_cov.iloc[:, 0]
data_cov_2 = data_cov.iloc[:, 2:]
data_cov = pd.concat([data_cov_1, data_cov_2], axis=1)
print(data_cov)
data_cov.to_csv('data_cov.csv', index=False)

print(data.columns)
factor_outcome = pd.DataFrame({'date': data_cov.iloc[95:, 0],
                               '信息': pd.Series(dtype='float64'),
                               '公用': pd.Series(dtype='float64'),
                               '医药': pd.Series(dtype='float64'),
                               '可选': pd.Series(dtype='float64'),
                               '工业': pd.Series(dtype='float64'),
                               '材料': pd.Series(dtype='float64'),
                               '消费': pd.Series(dtype='float64'),
                               '能源': pd.Series(dtype='float64'),
                               '通信': pd.Series(dtype='float64'),
                               '金融': pd.Series(dtype='float64')})
sigma_factor = []
# 第 95 期开始，到第 142 期结束，逐期构建最优投资组合。
for i in range(95, 143):
    print(data_cov.iloc[i, 0].strftime('%Y/%m')+"的最优投资组合：")
    # 期望超额收益率为10个行业超额收益率历史均值的平均值
    uhat = data_cov.iloc[0:i-1, 1:11].mean().mean()
    print("期望超额收益率为："+str(uhat))

    R = data_cov.iloc[0:i-1, 1:11]
    # 样本方差协方差矩阵
    Cov_Sample = np.array(np.cov(R, rowvar=False))

    # 常量估计法
    n = Cov_Sample.shape[0]
    variances = np.diag(Cov_Sample)  # (5,)
    avg_variance = np.mean(variances)  # 标量
    off_diag_mask = ~np.eye(n, dtype=bool)  # 非对角线位置的布尔掩码
    avg_covariance = np.mean(Cov_Sample[off_diag_mask])  # 标量
    Cov_Constant = np.full((n, n), avg_covariance)  # 全填平均协方差
    np.fill_diagonal(Cov_Constant, avg_variance)  # 对角线覆盖为平均方差

    # 因子模型估计法
    window = data_cov.iloc[0:i - 1]
    R = window.iloc[:, 1:11].values  # 资产收益，形状 (T, N)
    mkt = window['Rm'].values  # 市场因子，长度 T
    smb = window['SMB'].values  # SMB，长度 T
    hml = window['HML'].values  # HML，长度 T
    X = np.array(np.concatenate([
        np.ones((len(mkt) - 1, 1)),
        mkt[1:, None],
        smb[1:, None],
        hml[1:, None]
    ], axis=1))
    Y = np.array(R[1:])
    AB_hat = np.linalg.inv(X.T @ X) @ (X.T @ Y)
    ALPHA = AB_hat[0]  # 截距项，形状 (N,)
    BETA = AB_hat[1:4]  # 3×N 因子载荷矩阵（第1行：Rm，第2行：SMB，第3行：HML）
    RESD = Y - X @ AB_hat
    F = np.column_stack([mkt[1:], smb[1:], hml[1:]])  # T×3
    covfactor = np.cov(F, rowvar=False)  # 3×3
    covresidual = np.diag(np.diag(np.cov(RESD, rowvar=False)))
    Cov_Factor = BETA.T @ covfactor @ BETA + covresidual

    # 压缩估计法
    Sigma_t = Cov_Sample
    n = Sigma_t.shape[0]  # 资产个数
    T = data_cov.iloc[0:i - 1, 1:10].shape[0]  # 样本期数（时间长度）
    tr_Sigma = np.trace(Sigma_t)  # tr Σ_t
    tr_Sigma2 = np.trace(Sigma_t @ Sigma_t)  # tr(Σ_t^2)
    # 公式(20) 计算最优收缩强度 ρ
    numerator = (1 - 2 / n) * tr_Sigma2 + tr_Sigma ** 2
    denominator = (T - 2 / n) * (tr_Sigma2 - (tr_Sigma ** 2) / n)
    rho = numerator / denominator
    rho = min(rho, 1)  # 与 1 取较小值
    # 收缩目标 M = (tr Σ_t / n) * I
    M = (tr_Sigma / n) * np.eye(n)
    # 压缩估计
    Cov_Shrink = (1 - rho) * Sigma_t + rho * M
    # print("压缩估计法")
    # print(f"最优收缩强度 rho = {rho:.4f}")
    # print(Cov_Shrink)

    # 指数加权移动平均估计法 EWMA
    lambda_ = 0.94
    Cov_EWMA = np.cov(R, rowvar=False).copy()  # 用样本协方差当起点
    for t in range(len(R)):
        r_t = R[t, :][:, None]
        Cov_EWMA = lambda_ * Cov_EWMA + (1 - lambda_) * (r_t @ r_t.T)


    # 计算权重
    uhat = np.mean(R, axis=0)
    A = np.array(np.concatenate([uhat[:, None], np.ones((len(uhat), 1))], axis=1)).T
    up = np.mean(uhat)
    b = np.array(np.array([up, 1])[:, None])
    # 样本方差协方差矩阵
    omega_Sample = np.linalg.inv(Cov_Sample) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_Sample) @ A.T)) @ b
    # print("样本方差协方差矩阵下的权重")
    # print(omega_Sample.T)
    # 常量估计法
    omega_Constant = np.linalg.inv(Cov_Constant) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_Constant) @ A.T)) @ b
    # print("常量估计法下的权重")
    # print(omega_Constant.T)
    # 因子估计法
    omega_Factor = np.linalg.inv(Cov_Factor) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_Factor) @ A.T)) @ b
    # 这段代码是把计算出来的最优权重逐个写入结果表
    for j in range(10):
        factor_outcome.iloc[i - 95, j+1] = omega_Factor[j, 0]

    # print("因子估计法下的权重")
    # print(omega_Factor.T)
    # 压缩估计法
    omega_Shrink = np.linalg.inv(Cov_Shrink) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_Shrink) @ A.T)) @ b
    # print("压缩估计法下的权重")
    # print(omega_Shrink.T)
    # EWMA估计法
    omega_EWMA = np.linalg.inv(Cov_EWMA) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_EWMA) @ A.T)) @ b
    # print("EWMA估计法下的权重")
    # print(omega_EWMA.T)

    # 输出结果
    if i in [100, 114, 129]:
        print("样本方差协方差矩阵")
        print(Cov_Sample)
        print("样本方差协方差矩阵下的权重")
        print(omega_Sample.T)

        print("常量估计法")
        print(Cov_Constant)
        print("常量估计法下的权重")
        print(omega_Constant.T)

        print("因子模型估计法")
        print(Cov_Factor)
        print("因子估计法下的权重")
        print(omega_Factor.T)

        print("压缩估计法")
        print(f"最优收缩强度 rho = {rho:.4f}")
        print(Cov_Shrink)
        print("压缩估计法下的权重")
        print(omega_Shrink.T)

        print("EWMA估计法")
        print(Cov_EWMA)
        print("EWMA估计法下的权重")
        print(omega_EWMA.T)
    # 计算第四小题所需的标准差
    sigma = np.sqrt(omega_Factor.T@Cov_Factor@omega_Factor)
    print(sigma)
    sigma_factor.append(sigma[0, 0])

factor_outcome.reset_index(drop=True)
print(factor_outcome)


# 第二小题
# 堆叠面积图
dates = factor_outcome['date']
cols = ['信息', '公用', '医药', '可选', '工业', '材料', '消费', '能源', '通信', '金融']
plt.figure(1, figsize=(16, 9))
plt.stackplot(dates, *[factor_outcome[c] for c in cols], labels=cols, alpha=0.8)
plt.title('行业权重配置变化（因子模型估计法）', fontsize=36)
plt.ylabel('权重')
plt.xlabel('时间')
plt.ylim(0, 1)
# y 轴显示为百分比
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
# x 轴按年显示
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('行业权重配置变化时间序列图（因子模型估计法）_堆叠面积图.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 折线图
plt.figure(21, figsize=(16, 9))
for i in range(10):
    plt.plot(factor_outcome['date'], factor_outcome.iloc[:, i+1], lw=2)
plt.legend(['信息', '公用', '医药', '可选', '工业', '材料', '消费', '能源', '通信', '金融'])
plt.xlabel("时间")
plt.ylabel("权重")
plt.ylim([-1, 1])
plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0))
plt.title('行业权重配置变化（因子模型估计法）', fontsize=36)
plt.savefig('行业权重配置变化时间序列图（因子模型估计法）_折线图.jpg', dpi=300, bbox_inches='tight')
# plt.show()




# 第三小题
# 第2小题是给定收益目标，找风险最小的组合，不需要知道投资者的性格
# 第3小题是在收益和风险之间做主观权衡，找效用最大化组合（经济决策层面的效用最大化），因此必须引入相对风险规避系数 γ 来刻画有多讨厌风险
shrink_outcome = pd.DataFrame({'date': data_cov.iloc[95:, 0],
                               '信息': pd.Series(dtype='float64'),
                               '公用': pd.Series(dtype='float64'),
                               '医药': pd.Series(dtype='float64'),
                               '可选': pd.Series(dtype='float64'),
                               '工业': pd.Series(dtype='float64'),
                               '材料': pd.Series(dtype='float64'),
                               '消费': pd.Series(dtype='float64'),
                               '能源': pd.Series(dtype='float64'),
                               '通信': pd.Series(dtype='float64'),
                               '金融': pd.Series(dtype='float64')})
sigma_shrink = []
for i in range(95, 143):
    print(data_cov.iloc[i, 0].strftime('%Y/%m')+"的最优投资组合：")
    R = data_cov.iloc[0:i-1, 1:11]
    # 样本方差协方差矩阵
    Cov_Sample = np.array(np.cov(R, rowvar=False))
    # 因子模型估计法
    window = data_cov.iloc[0:i - 1]
    R = window.iloc[:, 1:11].values  # 资产收益，形状 (T, N)
    mkt = window['Rm'].values  # 市场因子，长度 T
    smb = window['SMB'].values  # SMB，长度 T
    hml = window['HML'].values  # HML，长度 T
    X = np.array(np.concatenate([
        np.ones((len(mkt) - 1, 1)),
        mkt[1:, None],
        smb[1:, None],
        hml[1:, None]
    ], axis=1))
    Y = np.array(R[1:])
    AB_hat = np.linalg.inv(X.T @ X) @ (X.T @ Y)
    ALPHA = AB_hat[0]  # 截距项，形状 (N,)
    BETA = AB_hat[1:4]  # 3×N 因子载荷矩阵（第1行：Rm，第2行：SMB，第3行：HML）
    RESD = Y - X @ AB_hat
    F = np.column_stack([mkt[1:], smb[1:], hml[1:]])  # T×3
    covfactor = np.cov(F, rowvar=False)  # 3×3
    covresidual = np.diag(np.diag(np.cov(RESD, rowvar=False)))
    Cov_Factor = BETA.T @ covfactor @ BETA + covresidual

    # 压缩估计法
    Sigma_t = Cov_Sample
    n = Sigma_t.shape[0]  # 资产个数
    T = data_cov.iloc[0:i - 1, 1:10].shape[0]  # 样本期数（时间长度）
    tr_Sigma = np.trace(Sigma_t)  # tr Σ_t
    tr_Sigma2 = np.trace(Sigma_t @ Sigma_t)  # tr(Σ_t^2)
    # 公式(20) 计算最优收缩强度 ρ
    numerator = (1 - 2 / n) * tr_Sigma2 + tr_Sigma ** 2
    denominator = (T - 2 / n) * (tr_Sigma2 - (tr_Sigma ** 2) / n)
    rho = numerator / denominator
    rho = min(rho, 1)  # 与 1 取较小值
    # 收缩目标 M = (tr Σ_t / n) * I
    M = (tr_Sigma / n) * np.eye(n)
    # 压缩估计
    Cov_Shrink = (1 - rho) * Sigma_t + rho * M
    # print("压缩估计法")
    # print(f"最优收缩强度 rho = {rho:.4f}")
    # print(Cov_Shrink)

    # 计算权重
    uhat = np.mean(R, axis=0)
    A = np.array(np.concatenate([uhat[:, None], np.ones((len(uhat), 1))], axis=1)).T
    up = np.mean(uhat)
    b = np.array(np.array([up, 1])[:, None])

    # 压缩估计法
    # 顺手算了一个最小方差权重
    omega_Shrink = np.linalg.inv(Cov_Shrink) @ A.T @ np.linalg.inv((A @ np.linalg.inv(Cov_Shrink) @ A.T)) @ b
    # 效用最大化
    gamma = 3.0
    Sigma_inv = np.linalg.inv(Cov_Shrink)
    mu = uhat.flatten()
    ones = np.ones(len(mu))
    c = ones @ Sigma_inv @ mu  # 1'Σ^{-1}μ
    d = ones @ Sigma_inv @ ones  # 1'Σ^{-1}1
    lambda_ = (c - gamma) / d
    omega_Utility = (Sigma_inv @ (mu - lambda_ * ones)) / gamma
    omega_Utility = omega_Utility.reshape(-1, 1)
    print(omega_Utility)
    for j in range(10):
        shrink_outcome.iloc[i - 95, j+1] = omega_Utility[j, 0]
    sigma = np.sqrt(omega_Utility.T @ Cov_Shrink @ omega_Utility)
    print(sigma)
    sigma_shrink.append(sigma[0, 0])

print(shrink_outcome)

# 堆叠面积图
dates = shrink_outcome['date']
cols = ['信息', '公用', '医药', '可选', '工业', '材料', '消费', '能源', '通信', '金融']
plt.figure(2, figsize=(16, 9))
plt.stackplot(dates, *[shrink_outcome[c] for c in cols], labels=cols, alpha=0.8)
plt.title('行业权重配置变化（压缩模型估计法）', fontsize=36)
plt.ylabel('权重')
plt.xlabel('时间')
plt.ylim(0, 1)
# y 轴显示为百分比
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
# x 轴按年显示
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('行业权重配置变化时间序列图（压缩模型估计法）_堆叠面积图.jpg', dpi=300, bbox_inches='tight')
# plt.show()
# 由于这里的限制条件只有一个，且没有做空限制，一些权重<0，这导致了了堆叠面积图不能很好地表示出结果
# 折线图
plt.figure(3, figsize=(16, 9))
for i in range(10):
    plt.plot(shrink_outcome['date'], shrink_outcome.iloc[:, i+1], lw=2)
plt.legend(['信息', '公用', '医药', '可选', '工业', '材料', '消费', '能源', '通信', '金融'])
plt.xlabel("时间")
plt.ylabel("权重")
plt.ylim([-3, 3])
plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0))
plt.title('行业权重配置变化（压缩模型估计法）', fontsize=36)
plt.savefig('行业权重配置变化时间序列图（压缩模型估计法）_折线图.jpg', dpi=300, bbox_inches='tight')
# plt.show()



# 现在得出的结论过于离谱，不妨画一下各个行业的累积超额
plt.figure(4, figsize=(16, 9))
plt.plot(data_cov['date'], data_cov['r1'].cumsum())
plt.plot(data_cov['date'], data_cov['r2'].cumsum())
plt.plot(data_cov['date'], data_cov['r3'].cumsum())
plt.plot(data_cov['date'], data_cov['r4'].cumsum())
plt.plot(data_cov['date'], data_cov['r5'].cumsum())
plt.plot(data_cov['date'], data_cov['r6'].cumsum())
plt.plot(data_cov['date'], data_cov['r7'].cumsum())
plt.plot(data_cov['date'], data_cov['r8'].cumsum())
plt.plot(data_cov['date'], data_cov['r9'].cumsum())
plt.plot(data_cov['date'], data_cov['r10'].cumsum())
plt.legend(['信息', '公用', '医药', '可选', '工业', '材料', '消费', '能源', '通信', '金融'], loc='lower left')
plt.xlabel("时间")
plt.ylabel("累积收益率")
plt.title("行业指数累积超额收益率", fontsize=36)
plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1.0))
plt.savefig('行业指数累积超额收益率.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 第四小题
# 需要用到上面已经计算好的factor_outcome和shrink_outcome两个最优权重
factor_outcome = factor_outcome.reset_index(drop=True)
print(factor_outcome)
shrink_outcome = shrink_outcome.reset_index(drop=True)
print(shrink_outcome)
# 一定要写drop=True，不然index会成为新的一列

# 因子估计法得到的最优权重对应的均值、标准差、夏普率
mu_factor = []
mu = 0
# 均值
for i in range(factor_outcome.shape[0]):
    for j in range(1, factor_outcome.shape[1]):
        mu += factor_outcome.iloc[i, j]*data_cov.iloc[i+95, j]
    mu_factor.append(mu)
    mu = 0
print(mu_factor)
print(len(mu_factor))
# 标准差
print(sigma_factor)
print(len(sigma_factor))
# 夏普比率
sharp_factor = []
for i in range(len(mu_factor)):
    sharp_factor.append(mu_factor[i]/sigma_factor[i])
print(sharp_factor)
print(np.mean(sharp_factor))


plt.figure(5, figsize=(16, 9))
plt.plot(factor_outcome['date'], mu_factor, lw=2)
plt.plot(factor_outcome['date'], sigma_factor, lw=2)
plt.plot(factor_outcome['date'], sharp_factor, lw=2)
plt.legend(['均值', '标准差', '夏普率'])
plt.title("样本外最优投资组合超额收益的描述性统计量(因子估计法)", fontsize=36)
plt.xlabel("时间")
plt.savefig('样本外最优投资组合超额收益的描述性统计量(因子估计法).jpg', dpi=300, bbox_inches='tight')


# 压缩估计法得到的最优权重对应的均值、标准差、夏普率
mu_shrink = []
mu = 0
# 均值
for i in range(shrink_outcome.shape[0]):
    for j in range(1, shrink_outcome.shape[1]):
        mu += shrink_outcome.iloc[i, j]*data_cov.iloc[i+95, j]
    mu_shrink.append(mu)
    mu = 0
print(mu_shrink)
print(len(mu_shrink))
# 标准差
print(sigma_shrink)
print(len(sigma_shrink))
# 夏普比率
sharp_shrink = []
for i in range(len(mu_shrink)):
    sharp_shrink.append(mu_shrink[i]/sigma_shrink[i])
print(sharp_shrink)
print(np.mean(sharp_shrink))

plt.figure(6, figsize=(16, 9))
plt.plot(shrink_outcome['date'], mu_shrink, lw=2)
plt.plot(shrink_outcome['date'], sigma_shrink, lw=2)
plt.plot(shrink_outcome['date'], sharp_shrink, lw=2)
plt.legend(['均值', '标准差', '夏普率'])
plt.title("样本外最优投资组合超额收益的描述性统计量(压缩估计法)", fontsize=36)
plt.xlabel("时间")
plt.savefig('样本外最优投资组合超额收益的描述性统计量(压缩估计法).jpg', dpi=300, bbox_inches='tight')

# 2010—2021年间，A股整体确实长期跑不赢无风险收益率，能源、材料等周期行业甚至大幅跑输，这是符合历史事实的