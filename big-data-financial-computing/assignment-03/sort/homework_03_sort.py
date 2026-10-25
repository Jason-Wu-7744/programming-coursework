import numpy as np
import pandas as pd

data = pd.read_csv('RESSET_MRESSTK_1.csv', encoding='GB2312', usecols=range(8))
# 用循环读数据
for i in range(2, 9):
    data_read = pd.read_csv('RESSET_MRESSTK_' + str(i) + '.csv', encoding='GB2312', usecols=range(8))
    data = pd.concat((data, data_read), axis=0, ignore_index=True)
    del data_read
# 区分市值与流通市值
data.columns = ['stk', 'date', 'close', 'fshare', 'tshare', 'monret', 'monrf', 'pe']
print(data)

data['date'] = pd.to_datetime(data['date'])
data['yearmonth'] = data['date'].dt.strftime('%Y%m').astype(int)
data['stksize'] = data['close']*data['fshare']
data['stkep'] = 1/data['pe']
data['monexcret'] = data['monret'] - data['monrf']
# subset 的意思是：只检查指定的列
data.dropna(inplace=True, subset=['stksize', 'stkep'])
print(data)

# 每月6月开始排
# 看有多少月份
uym = np.unique(data['yearmonth'].values)
print(len(uym))
print(uym)
# 按6月市值分组，再看后12月收益率

# 先按市值分组，再用β
class sort_portfolio:

    def __init__(self, data, months, gnum):
        self.data = data
        self.months = months
        self.gnum = gnum

    def data_months(self):
        dm = self.data.loc[self.data['yearmonth'] == self.months[0], ['stk', 'stksize', 'stkep']]
        dm.dropna(inplace=True)
        for i in range(1, len(self.months)):
            ind = self.data['yearmonth'] == self.months[i]
            dm = pd.merge(left=dm,
                          right=self.data.loc[ind, ['stk', 'monexcret']],
                          on='stk',
                          how='left',
                          sort=True,
                          suffixes=('', '_' + str(i)))
        dm.columns = ['stk', 'size6', 'ep6', 'ret7', 'ret8', 'ret9', 'ret10', 'ret11',
                      'ret12', 'retn1', 'retn2', 'retn3', 'retn4', 'retn5', 'retn6']
        return dm

    def sort_single_ind(self):
        L = np.sum(self.data['yearmonth'] == self.months[0])
        n = np.fix(L / self.gnum).astype(int)
        x = np.ones(L)
        i = 0
        while i < self.gnum:
            if i == self.gnum - 1:
                x[i * n:] = x[i * n:] * i
            else:
                x[i * n:(i + 1) * n] = x[i * n:(i + 1) * n] * i
            i = i + 1
        ssi = x.astype(int)
        return ssi

    def sort_double_ind(self):
        L = np.sum(self.data['yearmonth'] == self.months[0])
        l = np.fix(L / self.gnum).astype(int)
        n = np.fix(L / (self.gnum ** 2)).astype(int)
        x = np.ones(L)
        i = 0
        while i < self.gnum:
            j = 0
            while j < self.gnum:
                if j == self.gnum - 1:
                    if i == self.gnum - 1:
                        x[(i * l + j * n):] = x[(i * l + j * n):] * j
                    else:
                        x[(i * l + j * n):((i + 1) * l)] = x[(i * l + j * n):((i + 1) * l)] * j
                else:
                    x[(i * l + j * n):(i * l + (j + 1) * n)] = x[(i * l + j * n):(i * l + (j + 1) * n)] * j
                j = j + 1
            i = i + 1
        sdi = x.astype(int)
        return sdi

    def sequence_sort(self):
        dm = self.data_months()
        ssi = self.sort_single_ind()
        sdi = self.sort_double_ind()
        dm.sort_values(by=['size6'], ascending=True, inplace=True)
        dm['sinsort'] = ssi
        dm.sort_values(by=['sinsort', 'ep6'], ascending=[True, True], inplace=True)
        dm['dousort'] = sdi
        return dm

    def sequence_sort_mreturn(self):
        sp = self.sequence_sort()
        spmreturn = sp.loc[:, ['ret7', 'sinsort', 'dousort']].dropna().groupby(
            by=['sinsort', 'dousort'])['ret7'].mean()
        lret = ['ret8', 'ret9', 'ret10', 'ret11', 'ret12', 'retn1', 'retn2', 'retn3', 'retn4', 'retn5', 'retn6']
        for i in lret:
            a = sp.loc[:, [i, 'sinsort', 'dousort']].dropna().groupby(
                by=['sinsort', 'dousort'])[i].mean()
            spmreturn = pd.concat([spmreturn, a], axis=1)
        spmreturn['mret'] = spmreturn.apply(lambda x: x.mean(), axis=1)
        return spmreturn


# 2000/6-2001/6有哪些月份
print(uym[5:5+13])

sp = sort_portfolio(data, uym[5:5+13], 5)
# 先看2000年6月份所有股票在2000/6的市值以及后面12个月的市值
print(sp.data_months())
# 序贯排序，按市值分成5组，再按PE倒数各分为5组
print(sp.sequence_sort())
# 对每一组求平均
print(sp.sequence_sort_mreturn())

# 输出每一组结果
meanret = []
lcname = []
for i in range(5, 234, 12):
    # 每次截取13个连续月份
    # 第一个月分组，后12个月观察累积收益率
    if len(uym[i:i+13]) == 13:
        lcname.append(str(uym[i]))
        sp = sort_portfolio(data, uym[i:i+13], 5)
        spmreturn = sp.sequence_sort_mreturn()
        if len(meanret) == 0:
            meanret = spmreturn['mret']
        else:
            meanret = pd.concat([meanret, spmreturn['mret']], axis=1)
meanret.columns = lcname
print(meanret)


# 对所有年份求平均
meanret['meanreturn'] = meanret.apply(lambda x: x.mean(), axis=1)
a = meanret['meanreturn'].values.reshape((5,5))
print(a)

# 美化输出
print('{:>10s} {:>10s}, {:>10s}, {:>10s}, {:>10s}, {:>10s}'.format('', 'EP1', 'EP2', 'EP3', 'EP4', 'EP5'))
for i in range(5):
    print('{:>10s} {:10.5f}, {:10.5f}, {:10.5f}, {:10.5f}, {:10.5f}'.format('SIZE'+str(i+1),
                                                                            a[i, 0],
                                                                            a[i, 1],
                                                                            a[i, 2],
                                                                            a[i, 3],
                                                                            a[i, 4]))
