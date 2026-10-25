import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import f
import akshare as ak


index_dict = {"上证信息": "000039",
              "上证公用": "000007",
              "上证医药": "000037",
              "上证可选": "000035",
              "上证工业": "000034",
              "上证材料": "000033",
              "上证消费": "000036"}

# # 读取行业指数
# data_xinxi = pd.read_excel("000039.xlsx")
# data_xinxi.columns = ['date', 'close']
# data_xinxi['date'] = pd.to_datetime(data_xinxi['date'])
# data_xinxi.set_index('date', inplace=True)
# data_xinxi = data_xinxi.resample('W-FRI').last().reset_index()
# data_xinxi = data_xinxi.iloc[:-1, :]
# data_xinxi['r_xinxi'] = np.log(data_xinxi['close']) - np.log(data_xinxi['close']).shift(1)
# data_xinxi = data_xinxi.dropna()
# print(data_xinxi)
#
# data_gongyong = pd.read_excel("000007.xlsx")
# data_gongyong.columns = ['date', 'close']
# data_gongyong['date'] = pd.to_datetime(data_gongyong['date'])
# data_gongyong.set_index('date', inplace=True)
# data_gongyong = data_gongyong.resample('W-FRI').last().reset_index()
# data_gongyong = data_gongyong.iloc[:-1, :]
# data_gongyong['r_gongyong'] = np.log(data_gongyong['close']) - np.log(data_gongyong['close']).shift(1)
# data_gongyong = data_gongyong.dropna()
# print(data_gongyong)
#
# data_yiyao = pd.read_excel("000037.xlsx")
# data_yiyao.columns = ['date', 'close']
# data_yiyao['date'] = pd.to_datetime(data_yiyao['date'])
# data_yiyao.set_index('date', inplace=True)
# data_yiyao = data_yiyao.resample('W-FRI').last().reset_index()
# data_yiyao = data_yiyao.iloc[:-1, :]
# data_yiyao['r_yiyao'] = np.log(data_yiyao['close']) - np.log(data_yiyao['close']).shift(1)
# data_yiyao = data_yiyao.dropna()
# print(data_yiyao)
#
# data_kexuan = pd.read_excel("000035.xlsx")
# data_kexuan.columns = ['date', 'close']
# data_kexuan['date'] = pd.to_datetime(data_kexuan['date'])
# data_kexuan.set_index('date', inplace=True)
# data_kexuan = data_kexuan.resample('W-FRI').last().reset_index()
# data_kexuan = data_kexuan.iloc[:-1, :]
# data_kexuan['r_kexuan'] = np.log(data_kexuan['close']) - np.log(data_kexuan['close']).shift(1)
# data_kexuan = data_kexuan.dropna()
# print(data_kexuan)
#
# data_gongye= pd.read_excel("000034.xlsx")
# data_gongye.columns = ['date', 'close']
# data_gongye['date'] = pd.to_datetime(data_gongye['date'])
# data_gongye.set_index('date', inplace=True)
# data_gongye = data_gongye.resample('W-FRI').last().reset_index()
# data_gongye = data_gongye.iloc[:-1, :]
# data_gongye['r_gongye'] = np.log(data_gongye['close']) - np.log(data_gongye['close']).shift(1)
# data_gongye = data_gongye.dropna()
# print(data_gongye)
#
# data_cailiao = pd.read_excel("000033.xlsx")
# data_cailiao.columns = ['date', 'close']
# data_cailiao['date'] = pd.to_datetime(data_cailiao['date'])
# data_cailiao.set_index('date', inplace=True)
# data_cailiao = data_cailiao.resample('W-FRI').last().reset_index()
# data_cailiao = data_cailiao.iloc[:-1, :]
# data_cailiao['r_cailiao'] = np.log(data_cailiao['close']) - np.log(data_cailiao['close']).shift(1)
# data_cailiao = data_cailiao.dropna()
# print(data_cailiao)
#
# data_xiaofei = pd.read_excel("000036.xlsx")
# data_xiaofei.columns = ['date', 'close']
# data_xiaofei['date'] = pd.to_datetime(data_xiaofei['date'])
# data_xiaofei.set_index('date', inplace=True)
# data_xiaofei = data_xiaofei.resample('W-FRI').last().reset_index()
# data_xiaofei = data_xiaofei.iloc[:-1, :]
# data_xiaofei['r_xiaofei'] = np.log(data_xiaofei['close']) - np.log(data_xiaofei['close']).shift(1)
# data_xiaofei = data_xiaofei.dropna()
# print(data_xiaofei)
#
# # 读取大盘指数
# data_index = pd.read_excel("000001.xlsx")
# data_index.columns = ['date', 'close']
# data_index['date'] = pd.to_datetime(data_index['date'])
# data_index.set_index('date', inplace=True)
# data_index = data_index.resample('W-FRI').last().reset_index()
# data_index = data_index.iloc[:-1, :]
# print(data_index)
#
# # 读取无风险收益率
# data_rf_a = pd.read_excel("RESSET_DRESSTK_2016_2020_1.xlsx")
# data_rf_b = pd.read_excel("RESSET_DRESSTK_2021_2025_1.xlsx")
# data_rf = pd.concat([data_rf_a, data_rf_b], axis=0).reset_index(drop=True)
# data_rf.columns = ['date', 'rf']
# data_rf['date'] = pd.to_datetime(data_rf['date'])
# print(data_rf)
# # 日度数据转为周度
# data_rf.set_index('date', inplace=True)
# # 按周重采样，以每周五为截止日期，连乘
# data_rf = (1 + data_rf['rf']).resample('W-FRI').prod() - 1
# # 现在data_rf变为series
# data_rf = data_rf.iloc[:-1]
# print(data_rf)
# data_rf = data_rf.reset_index()
# data_rf.columns = ['date', 'rf']
# data_rf['date'] = pd.to_datetime(data_rf['date'])
# print(data_rf)
#
#
# # 下面导入三因子数据。从reset上现在的三因子数据种类十分齐全。包括了交易所标识（0沪深，1沪市，2深市）和市场标识（A股、B股、A+B股）
# # 鉴于现在选取的行业指数都是上证行业指数，所以选取沪市的A股
# # 所有的市值采用流通市值
# data_FF = pd.read_excel("RESSET_THRFACDAT_WEEKLY_1.xlsx")
# # print(data_FF)
# # print(data_FF.columns)
# data_FF = data_FF.iloc[:, 0:6]
# print(data_FF)
# print(data_FF.columns)
# data_FF.columns = ['exchange', 'market', 'date', 'MKT', 'SMB', 'HML']
# data_FF['date'] = pd.to_datetime(data_FF['date'])
# data_FF = data_FF[(data_FF['exchange'] == 1) & (data_FF['market'] == "A")].reset_index(drop=True)
# print(data_FF)
#
# # 合并数据
# data_matrix = pd.merge(left=data_FF[['date', 'MKT', 'SMB', 'HML']],
#                        right=data_rf,
#                        on=['date'],
#                        how='inner')
# print(data_matrix)
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_xinxi[['date', 'r_xinxi']],
#                        on=['date'],
#                        how='inner')
# print(data_matrix)
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_gongyong[['date', 'r_gongyong']],
#                        on=['date'],
#                        how='inner')
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_yiyao[['date', 'r_yiyao']],
#                        on=['date'],
#                        how='inner')
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_kexuan[['date', 'r_kexuan']],
#                        on=['date'],
#                        how='inner')
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_gongye[['date', 'r_gongye']],
#                        on=['date'],
#                        how='inner')
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_cailiao[['date', 'r_cailiao']],
#                        on=['date'],
#                        how='inner')
# data_matrix = pd.merge(left=data_matrix,
#                        right=data_xiaofei[['date', 'r_xiaofei']],
#                        on=['date'],
#                        how='inner')
# data_matrix.dropna(inplace=True)
# print(data_matrix)
# print(data_matrix.columns)
# data_matrix.to_csv("data_matrix.csv", index=False)



data_matrix = pd.read_csv("data_matrix.csv")
data_matrix['date'] = pd.to_datetime(data_matrix['date'])
print(data_matrix)

# 单资产检验-信息
x = data_matrix.loc[:, ['MKT', 'SMB', 'HML']].values
ret_rf = data_matrix.loc[:, ['rf']].values
ret_stock = data_matrix.loc[:, ['r_xinxi']].values
X = sm.add_constant(x)
Y = ret_stock - ret_rf
model = sm.OLS(Y, X)
results = model.fit()
print(results.summary())

# 单资产检验循环
reg_dict = {"上证信息": "r_xinxi",
            "上证公用": "r_gongyong",
            "上证医药": "r_yiyao",
            "上证可选": "r_kexuan",
            "上证工业": "r_gongye",
            "上证材料": "r_cailiao",
            "上证消费": "r_xiaofei"}
for i in range(len(reg_dict)):
    print("对"+list(reg_dict.keys())[i]+"进行FF三因子单资产检验：")
    x = data_matrix.loc[:, ['MKT', 'SMB', 'HML']].values
    ret_rf = data_matrix.loc[:, ['rf']].values
    ret_stock = data_matrix.loc[:, [list(reg_dict.values())[i]]].values
    X = sm.add_constant(x)
    Y = ret_stock - ret_rf
    model = sm.OLS(Y, X)
    results = model.fit()
    print(results.summary())
    print("\n")

# 下面开始三因子多资产检验
T = len(Y)
N = 7
K = 3
y = data_matrix.iloc[:, 5:12].values - data_matrix.loc[:, ['rf']].values
x = data_matrix.loc[:, ['MKT', 'SMB', 'HML']].values
# 加常数项
x = sm.add_constant(x)
xTx = np.dot(np.transpose(x), x)
xTy = np.dot(np.transpose(x), y)
AB_hat = np.dot(np.linalg.inv(xTx), xTy)
ALPHA = AB_hat[0]
print(ALPHA)
RESD = y - np.dot(x, AB_hat)
COV = np.dot(np.transpose(RESD), RESD)/T
invCOV = np.linalg.inv(COV)

fs = x[:, [1, 2, 3]]
muhat = np.mean(fs, axis=0).reshape((3, 1))
fs = fs - np.mean(fs, axis=0)
omegahat = np.dot(np.transpose(fs), fs)/T
invOMG = np.linalg.inv(omegahat)

xxx = np.dot(np.dot(np.transpose(muhat), invOMG), muhat)
yyy = np.dot(np.dot(ALPHA, invCOV), np.transpose(ALPHA))
GRS = (T-N-K)/N*(1/(1+xxx))*yyy
pvalue = 1 - f.cdf(GRS[0][0], N, T-N-K)

print('三因子模型的GRS多资产检验结果')
# 输出: " alpha1"（右对齐，宽度7）
print('{:>7s},{:>7s},{:>7s},{:>7s},{:>7s},{:>7s},{:>7s},{:>7s},{:>7s}'.format('alpha1', 'alpha2', 'alpha3', 'alpha4', 'alpha5', 'alpha6', 'alpha7', 'GRS', 'pvalue'))
print('{:7.4f},{:7.4f},{:7.4f},{:7.4f},{:7.4f},{:7.4f},{:7.4f},{:7.4f},{:7.4f}'.format(ALPHA[0], ALPHA[1], ALPHA[2], ALPHA[3], ALPHA[4], ALPHA[5], ALPHA[6], GRS[0][0], pvalue))

