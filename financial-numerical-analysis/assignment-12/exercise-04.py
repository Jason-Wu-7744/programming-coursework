# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

data = pd.read_excel('Exp12-Python-实验数据-对数正态分布数据样本.xlsx')
data.columns = ['x']
data['lnx'] = np.log(data['x'])
print(data)

# 第一小题
# 通过对取对之后的似然函数的mu求导可以发现，mu的估计值就是lnx.mean
mu = data['lnx'].mean()
print("mu=", mu)
# 同理可得sigma的估计值就是lnx.std。实际上我们把lnx看作服从标准正态，从而利用标准正态的极大似然估计来简便地算出mu和sigma。
# 当然，用极大似然函数取对再求导也可以得出一样的mu、sigma估计值
sigma = data['lnx'].std()
print("sigma=", sigma)

# 第二小题
def integral_fun(x):
    f = np.e**(-(np.log(x)-mu)**2/2/sigma**2)/(x*np.sqrt(2*np.pi)*sigma)
    return f

def integral_simpson(a, b, n):
    x_0 = a
    x_n = b
    h = (x_n - x_0)/n
    xp = np.arange(x_0, x_n+h, h)
    fxp = integral_fun(xp)
    fxp[1:-1:2] = fxp[1:-1:2]*4
    fxp[2:-1:2] = fxp[2:-1:2]*2
    Sn = np.sum(fxp)*h/3
    return Sn

S = 1 - integral_simpson(0.01, 5, 10)
# 复合辛普森法的区间只能为偶数，故这里代入10而不是题目给出的9
# 此外，还出现了一个问题，对数不能真的从0开始，所以截断从0.01开始积分。
# 还有一个更加值得注意的问题。如果从0.000001开始积分，得出的S会是-32这样的不合理的值。这可能是由于对数正态在 x→0⁺ 时密度趋于 ∞导致的，具体的原因有待后续的学习。
# 左端点从0.1到0.01时，S就从0.7变为了0.22
print('存函数的计算值为：', S)