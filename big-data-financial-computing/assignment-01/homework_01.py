import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
plt.rcParams.update({
    "font.family": "Microsoft YaHei",  # 改用微软雅黑
    "font.size": 20,
    "axes.unicode_minus": False
})

# 1.读取数据

# mat_data = scipy.io.loadmat('4实验数据-SSEC_min.mat')
# print(mat_data.keys())

# 此时输出的结果为dict_keys(['__header__', '__version__', '__globals__', 'd', 'p', 't'])
# 只有d/p/t三个是有效的变量

# data = pd.DataFrame({'Date': mat_data['d'].squeeze(),
#                      'Time': mat_data['t'].squeeze(),
#                      'Price': mat_data['p'].squeeze()})
# print(data.head())
# data.to_csv('data_price.csv', index=False)

data = pd.read_csv('data_price.csv')
print(data)
data['Date'] = data['Date'].str.strip("[]").str.strip("'")
data['Time'] = data['Time'].str.strip("[]").str.strip("'")
# print(data)
data['Date'] = pd.to_datetime(data['Date'], format='mixed')
data['Time'] = pd.to_datetime(data['Time'], format='mixed').dt.time
# print(data)
data['DateTime'] = data['Date'] + pd.to_timedelta(data['Time'].astype(str))
# print(data)
# 可以看到前五行为一些零散的日度数据，对于计算日内收益率没有帮助，所以可以将前五行删去
data = data.iloc[5:].reset_index(drop=True)
# print(data)
# 计算对数价格
data['lnP'] = np.log(data['Price'])
print(data)
# 清理对数价格以防止出现无穷大的lnp影响拟合正态
data = data[np.isfinite(data['lnP'])].reset_index(drop=True)


#画图观看效果
# plt.subplot(2, 1, 1)
# plt.plot(data['DateTime'], data['Price'])
# plt.subplot(2, 1, 2)
# plt.plot(data['DateTime'], data['lnP'])
# plt.show()

# 2.计算经验概率密度
bin = np.linspace(-0.1, 0.1, 21)
bin_plt = np.linspace(-0.098, 0.098, 20)


# minutes_1 = []
# for i in range(len(data['DateTime'])-1):
#     if data['DateTime'][i+1]-data['DateTime'][i] == pd.Timedelta('1 minute'):
#         minutes_1.append(data['lnP'][i+1]-data['lnP'][i])
# print(len(minutes_1))
#
# f = np.arange(len(bin)-1)
# for j in range(len(bin)-1):
#     f[j] = np.sum((minutes_1 >= bin[j]) & (minutes_1 < bin[j+1]))

time_diff = data['DateTime'].diff()

# 1min
minutes_1 = data['lnP'].diff(1).dropna()
print(minutes_1)
f_1 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_1[j] = np.sum((minutes_1 >= bin[j]) & (minutes_1 < bin[j+1]))
print(f_1)
p_1 = f_1/len(minutes_1)/np.diff(bin)
print(p_1)
plt.figure(1, figsize=(12, 7))
plt.semilogy(bin_plt, p_1, 'b-o')
# mu, sigma = scipy.stats.norm.fit(p_1)
# 用p_1这个概率密度值去拟合是绝对错误的，必须使用monutes_1这个原始数据
mu_1, sigma_1 = scipy.stats.norm.fit(minutes_1)
print(mu_1, sigma_1)
# 拟合出的正态分布过于巨大，故缩小正态的显示范围
x_show_1 = np.linspace(-0.005, 0.005, 20)
norm_plt = scipy.stats.norm.pdf(x_show_1, loc=mu_1, scale=sigma_1)
plt.semilogy(x_show_1, norm_plt)
plt.title("1分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('1分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 后续采用滑动窗口而非跳跃窗口
# 5min
minutes_5 = data['lnP'].diff(5).dropna()
print(minutes_5)
f_5 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_5[j] = np.sum((minutes_5 >= bin[j]) & (minutes_5 < bin[j+1]))
print(f_5)
p_5 = f_5/len(minutes_5)/np.diff(bin)
print(p_5)
plt.figure(5, figsize=(12, 7))
plt.semilogy(bin_plt, p_5, 'g--s')
mu_5, sigma_5 = scipy.stats.norm.fit(minutes_5)
print(mu_5, sigma_5)
x_show_5 = np.linspace(-0.014, 0.014, 20)
norm_plt = scipy.stats.norm.pdf(x_show_5, loc=mu_5, scale=sigma_5)
plt.semilogy(x_show_5, norm_plt)
plt.title("5分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('5分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 10min
minutes_10 = data['lnP'].diff(10).dropna()
print(minutes_10)
f_10 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_10[j] = np.sum((minutes_10 >= bin[j]) & (minutes_10 < bin[j+1]))
print(f_10)
p_10 = f_10/len(minutes_10)/np.diff(bin)
print(p_10)
plt.figure(10, figsize=(12, 7))
plt.semilogy(bin_plt, p_10, 'r-^')
mu_10, sigma_10 = scipy.stats.norm.fit(minutes_10)
print(mu_10, sigma_10)
x_show_10 = np.linspace(-0.017, 0.017, 20)
norm_plt = scipy.stats.norm.pdf(x_show_10, loc=mu_10, scale=sigma_10)
plt.semilogy(x_show_10, norm_plt)
plt.title("10分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('10分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 30min
minutes_30 = data['lnP'].diff(30).dropna()
print(minutes_30)
f_30 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_30[j] = np.sum((minutes_30 >= bin[j]) & (minutes_30 < bin[j+1]))
print(f_30)
p_30 = f_30/len(minutes_30)/np.diff(bin)
print(p_30)
plt.figure(30, figsize=(12, 7))
plt.semilogy(bin_plt, p_30, 'c:v')
mu_30, sigma_30 = scipy.stats.norm.fit(minutes_30)
print(mu_30, sigma_30)
x_show_30 = np.linspace(-0.03, 0.03, 20)
norm_plt = scipy.stats.norm.pdf(x_show_30, loc=mu_30, scale=sigma_30)
plt.semilogy(x_show_30, norm_plt)
plt.title("30分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('30分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 60min
minutes_60 = data['lnP'].diff(60).dropna()
print(minutes_60)
f_60 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_60[j] = np.sum((minutes_60 >= bin[j]) & (minutes_60 < bin[j+1]))
print(f_60)
p_60 = f_60/len(minutes_60)/np.diff(bin)
print(p_60)
plt.figure(60, figsize=(12, 7))
plt.semilogy(bin_plt, p_60, 'm-.d')
mu_60, sigma_60 = scipy.stats.norm.fit(minutes_60)
print(mu_60, sigma_60)
x_show_60 = np.linspace(-0.04, 0.04, 20)
norm_plt = scipy.stats.norm.pdf(x_show_60, loc=mu_60, scale=sigma_60)
plt.semilogy(x_show_60, norm_plt)
plt.title("60分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('60分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 120min
minutes_120 = data['lnP'].diff(120).dropna()
print(minutes_120)
f_120 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_120[j] = np.sum((minutes_120 >= bin[j]) & (minutes_120 < bin[j+1]))
print(f_120)
p_120 = f_120/len(minutes_120)/np.diff(bin)
print(p_120)
plt.figure(120, figsize=(12, 7))
plt.semilogy(bin_plt, p_120, 'y--*')
mu_120, sigma_120 = scipy.stats.norm.fit(minutes_120)
print(mu_120, sigma_120)
x_show_120 = np.linspace(-0.057, 0.057, 20)
norm_plt = scipy.stats.norm.pdf(x_show_120, loc=mu_120, scale=sigma_120)
plt.semilogy(x_show_120, norm_plt)
plt.title("120分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('120分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 240min
minutes_240 = data['lnP'].diff(240).dropna()
print(minutes_240)
f_240 = np.zeros(len(bin)-1)
for j in range(len(bin)-1):
    f_240[j] = np.sum((minutes_240 >= bin[j]) & (minutes_240 < bin[j+1]))
print(f_240)
p_240 = f_240/len(minutes_240)/np.diff(bin)
print(p_240)
plt.figure(240, figsize=(12, 7))
plt.semilogy(bin_plt, p_240, 'k-p')
mu_240, sigma_240 = scipy.stats.norm.fit(minutes_240)
print(mu_240, sigma_240)
x_show_240 = np.linspace(-0.08, 0.08, 20)
norm_plt = scipy.stats.norm.pdf(x_show_240, loc=mu_240, scale=sigma_240)
plt.semilogy(x_show_240, norm_plt)
plt.title("240分钟收益率的正态拟合分布及其经验概率密度对比图")
plt.legend(['经验概率密度', '正态拟合分布'], loc='upper right')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('240分钟收益率的正态拟合分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()

print("----------------------------------------------------------------------------------------------------------------")

# 下面开始考虑尾部分布特征
# plt.figure(2)
# plt.loglog(p_240)
# plt.show()

# 1min
print("1min")
# # 若用标准差来判断尾部
sigma_1 = minutes_1.std()
# # minutes_1.std() 默认是样本标准差（ddof=1，分母为 n−1 ）
threshold = 2 * sigma_1
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_1), 99)   # 统一取绝对值最大的 1%
pos_1 = minutes_1[minutes_1 > threshold]
# pos_1 = minutes_1[minutes_1 > 0]
print("pos_1")
print(pos_1)
neg_1 = minutes_1[minutes_1 < -threshold]
# neg_1 = minutes_1[minutes_1 < 0]
# 幂律分布定义在正实数域上，我们需要将负收益转换为可分析的形式。
neg_1 = np.abs(neg_1)
print("neg_1")
print(neg_1)
bin_log = np.logspace(np.log10(threshold), -1, 11)
# bin_log = np.logspace(-4, -1, 21)
#取对数中点
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
f_1_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_1_pos[j] = np.sum((pos_1 >= bin_log[j]) & (pos_1 < bin_log[j+1]))
print("f_1_pos")
print(f_1_pos)
p_1_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_1_pos[i] = f_1_pos[i]/len(pos_1)/(bin_log[i+1]-bin_log[i])
print("p_1_pos")
print(p_1_pos)
f_1_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_1_neg[j] = np.sum((neg_1 >= bin_log[j]) & (neg_1 < bin_log[j+1]))
print("f_1_neg")
print(f_1_neg)
p_1_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_1_neg[i] = f_1_neg[i]/len(neg_1)/(bin_log[i+1]-bin_log[i])
print("p_1_neg")
print(p_1_neg)
plt.figure(11, figsize=(12, 7))
plt.loglog(bin_log_plt, p_1_pos, 'ro')
plt.loglog(bin_log_plt, p_1_neg, 'bs')
# plt.show()
# 开始回归拟合
log_bin_log_plt = np.log(bin_log_plt)
log_p_1_pos = np.log(p_1_pos)
coef_1_pos = np.polyfit(log_bin_log_plt, log_p_1_pos, deg=1)
print("coef_1_pos")
print(coef_1_pos)
y_show_1_pos = bin_log_plt**(coef_1_pos[0])*np.e**coef_1_pos[1]
plt.loglog(bin_log_plt, y_show_1_pos, 'r')
log_p_1_neg = np.log(p_1_neg)
coef_1_neg = np.polyfit(log_bin_log_plt, log_p_1_neg, deg=1)
print("coef_1_neg")
print(coef_1_neg)
y_show_1_neg = bin_log_plt**(coef_1_neg[0])*np.e**coef_1_neg[1]
plt.loglog(bin_log_plt, y_show_1_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('1分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_1_pos[0]))
plt.text(10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_1_neg[0]))
plt.savefig('1分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 5min
sigma_5 = minutes_5.std()
threshold = 2 * sigma_5
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_5), 99)
pos_5 = minutes_5[minutes_5 > threshold]
print(pos_5)
neg_5 = minutes_5[minutes_5 < -threshold]
neg_5 = np.abs(neg_5)
print(neg_5)
bin_log = np.logspace(np.log10(threshold), -1, 11)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
log_bin_log_plt = np.log(bin_log_plt)
f_5_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_5_pos[j] = np.sum((pos_5 >= bin_log[j]) & (pos_5 < bin_log[j+1]))
print(f_5_pos)
p_5_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_5_pos[i] = f_5_pos[i]/len(pos_5)/(bin_log[i+1]-bin_log[i])
print(p_5_pos)
f_5_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_5_neg[j] = np.sum((neg_5 >= bin_log[j]) & (neg_5 < bin_log[j+1]))
print(f_5_neg)
p_5_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_5_neg[i] = f_5_neg[i]/len(neg_5)/(bin_log[i+1]-bin_log[i])
print(p_5_neg)
plt.figure(15, figsize=(12, 7))
plt.loglog(bin_log_plt, p_5_pos, 'ro')
plt.loglog(bin_log_plt, p_5_neg, 'bs')
# 开始回归拟合
log_p_5_pos = np.log(p_5_pos)
coef_5_pos = np.polyfit(log_bin_log_plt, log_p_5_pos, deg=1)
print(coef_5_pos)
y_show_5_pos = bin_log_plt**(coef_5_pos[0])*np.e**coef_5_pos[1]
plt.loglog(bin_log_plt, y_show_5_pos, 'r')
log_p_5_neg = np.log(p_5_neg)
coef_5_neg = np.polyfit(log_bin_log_plt, log_p_5_neg, deg=1)
print(coef_5_neg)
y_show_5_neg = bin_log_plt**(coef_5_neg[0])*np.e**coef_5_neg[1]
plt.loglog(bin_log_plt, y_show_5_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('5分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_5_pos[0]))
plt.text(10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_5_neg[0]))
plt.savefig('5分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 10min
sigma_10 = minutes_10.std()
threshold = 2 * sigma_10
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_10), 99)
pos_10 = minutes_10[minutes_10 > threshold]
print(pos_10)
neg_10 = minutes_10[minutes_10 < -threshold]
neg_10 = np.abs(neg_10)
print(neg_10)
bin_log = np.logspace(np.log10(threshold), -1, 11)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
log_bin_log_plt = np.log(bin_log_plt)
f_10_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_10_pos[j] = np.sum((pos_10 >= bin_log[j]) & (pos_10 < bin_log[j+1]))
print(f_10_pos)
p_10_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_10_pos[i] = f_10_pos[i]/len(pos_10)/(bin_log[i+1]-bin_log[i])
print(p_10_pos)
f_10_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_10_neg[j] = np.sum((neg_10 >= bin_log[j]) & (neg_10 < bin_log[j+1]))
print(f_10_neg)
p_10_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_10_neg[i] = f_10_neg[i]/len(neg_10)/(bin_log[i+1]-bin_log[i])
print(p_10_neg)
plt.figure(110, figsize=(12, 7))
plt.loglog(bin_log_plt, p_10_pos, 'ro')
plt.loglog(bin_log_plt, p_10_neg, 'bs')
# 开始回归拟合
log_p_10_pos = np.log(p_10_pos)
coef_10_pos = np.polyfit(log_bin_log_plt, log_p_10_pos, deg=1)
print(coef_10_pos)
y_show_10_pos = bin_log_plt**(coef_10_pos[0])*np.e**coef_10_pos[1]
plt.loglog(bin_log_plt, y_show_10_pos, 'r')
log_p_10_neg = np.log(p_10_neg)
coef_10_neg = np.polyfit(log_bin_log_plt, log_p_10_neg, deg=1)
print(coef_10_neg)
y_show_10_neg = bin_log_plt**(coef_10_neg[0])*np.e**coef_10_neg[1]
plt.loglog(bin_log_plt, y_show_10_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('10分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_10_pos[0]))
plt.text(10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_10_neg[0]))
plt.savefig('10分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 30min
sigma_30 = minutes_30.std()
threshold = 2 * sigma_30
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_30), 99)
pos_30 = minutes_30[minutes_30 > threshold]
print(pos_30)
neg_30 = minutes_30[minutes_30 < -threshold]
neg_30 = np.abs(neg_30)
print(neg_30)
bin_log = np.logspace(np.log10(threshold), -1, 11)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
log_bin_log_plt = np.log(bin_log_plt)
f_30_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_30_pos[j] = np.sum((pos_30 >= bin_log[j]) & (pos_30 < bin_log[j+1]))
print(f_30_pos)
p_30_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_30_pos[i] = f_30_pos[i]/len(pos_30)/(bin_log[i+1]-bin_log[i])
print(p_30_pos)
f_30_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_30_neg[j] = np.sum((neg_30 >= bin_log[j]) & (neg_30 < bin_log[j+1]))
print(f_30_neg)
p_30_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_30_neg[i] = f_30_neg[i]/len(neg_30)/(bin_log[i+1]-bin_log[i])
print(p_30_neg)
plt.figure(130, figsize=(12, 7))
plt.loglog(bin_log_plt, p_30_pos, 'ro')
plt.loglog(bin_log_plt, p_30_neg, 'bs')
# 开始回归拟合
log_p_30_pos = np.log(p_30_pos)
coef_30_pos = np.polyfit(log_bin_log_plt, log_p_30_pos, deg=1)
print(coef_30_pos)
y_show_30_pos = bin_log_plt**(coef_30_pos[0])*np.e**coef_30_pos[1]
plt.loglog(bin_log_plt, y_show_30_pos, 'r')
log_p_30_neg = np.log(p_30_neg)
coef_30_neg = np.polyfit(log_bin_log_plt, log_p_30_neg, deg=1)
print(coef_30_neg)
y_show_30_neg = bin_log_plt**(coef_30_neg[0])*np.e**coef_30_neg[1]
plt.loglog(bin_log_plt, y_show_30_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('30分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_30_pos[0]))
plt.text(10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_30_neg[0]))
plt.savefig('30分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 60min
sigma_60 = minutes_60.std()
threshold = 2 * sigma_60
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_60), 99)
pos_60 = minutes_60[minutes_60 > threshold]
print(pos_60)
neg_60 = minutes_60[minutes_60 < -threshold]
neg_60 = np.abs(neg_60)
print(neg_60)
bin_log = np.logspace(np.log10(threshold), -1, 11)
log_bin_log_plt = np.log(bin_log_plt)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
f_60_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_60_pos[j] = np.sum((pos_60 >= bin_log[j]) & (pos_60 < bin_log[j+1]))
print(f_60_pos)
p_60_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_60_pos[i] = f_60_pos[i]/len(pos_60)/(bin_log[i+1]-bin_log[i])
print(p_60_pos)
f_60_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_60_neg[j] = np.sum((neg_60 >= bin_log[j]) & (neg_60 < bin_log[j+1]))
print(f_60_neg)
p_60_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_60_neg[i] = f_60_neg[i]/len(neg_60)/(bin_log[i+1]-bin_log[i])
print(p_60_neg)
plt.figure(160, figsize=(12, 7))
plt.loglog(bin_log_plt, p_60_pos, 'ro')
plt.loglog(bin_log_plt, p_60_neg, 'bs')
# 开始回归拟合
log_p_60_pos = np.log(p_60_pos)
coef_60_pos = np.polyfit(log_bin_log_plt, log_p_60_pos, deg=1)
print(coef_60_pos)
y_show_60_pos = bin_log_plt**(coef_60_pos[0])*np.e**coef_60_pos[1]
plt.loglog(bin_log_plt, y_show_60_pos, 'r')
log_p_60_neg = np.log(p_60_neg)
coef_60_neg = np.polyfit(log_bin_log_plt, log_p_60_neg, deg=1)
print(coef_60_neg)
y_show_60_neg = bin_log_plt**(coef_60_neg[0])*np.e**coef_60_neg[1]
plt.loglog(bin_log_plt, y_show_60_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('60分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(10**(-1.5), 10**(-2), r'$-\alpha_{pos}$='+str(coef_60_pos[0]))
plt.text(10**(-1.5), 10**(-3), r'$-\alpha_{neg}$='+str(coef_60_neg[0]))
plt.savefig('60分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()

# 120min
sigma_120 = minutes_120.std()
threshold = 2 * sigma_120
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_120), 99)
pos_120 = minutes_120[minutes_120 > threshold]
print(pos_120)
neg_120 = minutes_120[minutes_120 < -threshold]
neg_120 = np.abs(neg_120)
print(neg_120)
bin_log = np.logspace(np.log10(threshold), -1, 11)
log_bin_log_plt = np.log(bin_log_plt)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
f_120_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_120_pos[j] = np.sum((pos_120 >= bin_log[j]) & (pos_120 < bin_log[j+1]))
print(f_120_pos)
p_120_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_120_pos[i] = f_120_pos[i]/len(pos_120)/(bin_log[i+1]-bin_log[i])
print(p_120_pos)
f_120_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_120_neg[j] = np.sum((neg_120 >= bin_log[j]) & (neg_120 < bin_log[j+1]))
print(f_120_neg)
p_120_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_120_neg[i] = f_120_neg[i]/len(neg_120)/(bin_log[i+1]-bin_log[i])
print(p_120_neg)
plt.figure(1120, figsize=(12, 7))
plt.loglog(bin_log_plt, p_120_pos, 'ro')
plt.loglog(bin_log_plt, p_120_neg, 'bs')
# 开始回归拟合
log_p_120_pos = np.log(p_120_pos)
coef_120_pos = np.polyfit(log_bin_log_plt, log_p_120_pos, deg=1)
print(coef_120_pos)
y_show_120_pos = bin_log_plt**(coef_120_pos[0])*np.e**coef_120_pos[1]
plt.loglog(bin_log_plt, y_show_120_pos, 'r')
log_p_120_neg = np.log(p_120_neg)
coef_120_neg = np.polyfit(log_bin_log_plt, log_p_120_neg, deg=1)
print(coef_120_neg)
y_show_120_neg = bin_log_plt**(coef_120_neg[0])*np.e**coef_120_neg[1]
plt.loglog(bin_log_plt, y_show_120_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('120分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(3*10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_120_pos[0]))
plt.text(3*10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_120_neg[0]))
plt.savefig('120分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 240min
sigma_240 = minutes_240.std()
threshold = 2 * sigma_240
# 使用分位数判断尾部
# threshold = np.percentile(np.abs(minutes_240), 99)
pos_240 = minutes_240[minutes_240 > threshold]
print(pos_240)
neg_240 = minutes_240[minutes_240 < -threshold]
neg_240 = np.abs(neg_240)
print(neg_240)
bin_log = np.logspace(np.log10(threshold), -1, 11)
log_bin_log_plt = np.log(bin_log_plt)
bin_log_plt = np.sqrt(bin_log[:-1] * bin_log[1:])
f_240_pos = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_240_pos[j] = np.sum((pos_240 >= bin_log[j]) & (pos_240 < bin_log[j+1]))
print(f_240_pos)
p_240_pos = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_240_pos[i] = f_240_pos[i]/len(pos_240)/(bin_log[i+1]-bin_log[i])
print(p_240_pos)
f_240_neg = np.zeros(len(bin_log)-1)
for j in range(len(bin_log)-1):
    f_240_neg[j] = np.sum((neg_240 >= bin_log[j]) & (neg_240 < bin_log[j+1]))
print(f_240_neg)
p_240_neg = np.zeros(len(bin_log)-1)
for i in range(len(bin_log)-1):
    p_240_neg[i] = f_240_neg[i]/len(neg_240)/(bin_log[i+1]-bin_log[i])
print(p_240_neg)
plt.figure(1240, figsize=(12, 7))
plt.loglog(bin_log_plt, p_240_pos, 'ro')
plt.loglog(bin_log_plt, p_240_neg, 'bs')
# 开始回归拟合
log_p_240_pos = np.log(p_240_pos)
coef_240_pos = np.polyfit(log_bin_log_plt, log_p_240_pos, deg=1)
print(coef_240_pos)
y_show_240_pos = bin_log_plt**(coef_240_pos[0])*np.e**coef_240_pos[1]
plt.loglog(bin_log_plt, y_show_240_pos, 'r')
log_p_240_neg = np.log(p_240_neg)
coef_240_neg = np.polyfit(log_bin_log_plt, log_p_240_neg, deg=1)
print(coef_240_neg)
y_show_240_neg = bin_log_plt**(coef_240_neg[0])*np.e**coef_240_neg[1]
plt.loglog(bin_log_plt, y_show_240_neg, 'b')
plt.legend(['正尾', '负尾'], loc='upper right')
plt.yticks([10**(-4), 10**(-2), 10**0, 10**2, 10**4])
plt.title('240分钟收益率的尾部拟合幂律分布及其经验概率密度对比图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.text(4*10**(-2), 10**(-2), r'$-\alpha_{pos}$='+str(coef_240_pos[0]))
plt.text(4*10**(-2), 10**(-3), r'$-\alpha_{neg}$='+str(coef_240_neg[0]))
plt.savefig('240分钟收益率的尾部拟合幂律分布及其经验概率密度对比图.jpg', dpi=300, bbox_inches='tight')
# plt.show()


# 输出结果文件
plt.figure(721, figsize=(16, 9))
plt.semilogy(bin_plt, p_1, 'b-o')
plt.semilogy(bin_plt, p_5, 'g--s')
plt.semilogy(bin_plt, p_10, 'r-^')
plt.semilogy(bin_plt, p_30, 'c:v')
plt.semilogy(bin_plt, p_60, 'm-.d')
plt.semilogy(bin_plt, p_120, 'y--*')
plt.semilogy(bin_plt, p_240, 'k-p')
plt.legend(['1min', '5min', '10min', '30min', '60min', '120min', '240min'])
plt.title('不同尺度收益率的经验概率密度散点图')
plt.xlabel('收益率r')
plt.ylabel('经验概率密度p(r)')
plt.yticks(np.logspace(-4, 2, 7))
plt.savefig('不同尺度收益率的经验概率密度散点图.jpg', dpi=300, bbox_inches='tight')
plt.show()



# 以上按照标准差来判断尾部与否，事实上，如果使用分位数来判断尾部，时间尺度上升，alpha应该单调下降