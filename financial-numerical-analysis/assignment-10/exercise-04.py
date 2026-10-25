# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

def Interp_Newton(x, fx, xval):
    N = len(x)
    duoxiangshi = np.ones([len(xval), N])   # 给每个函数项赋初值
    chashang = np.zeros([N, N+1])           # 给差商赋初值
    chashang[:, 0] = x
    chashang[:, 1] = fx
    for i in range(2, N+1):
        chashang[i-1:, i] = (chashang[i-1:, i-1] - chashang[i-2:-1, i-1])/(chashang[i-1:, 0] - chashang[0:-1-i+2, 0])
        duoxiangshi[:, i-1] = duoxiangshi[:, i-2] * (xval - x[i-2])
    table_cs = chashang[1:, 2:]             # 得出差商表
    chashang = chashang[:, 1:]
    newton_xishu = np.diag(chashang)        # 得出牛顿系数项
    yval = np.zeros(len(xval))
    for i in range(len(xval)):
        yval[i] = np.sum(duoxiangshi[i, :] * newton_xishu)  # 得出该多项式在每一点的函数值
    return table_cs, newton_xishu, duoxiangshi, yval
# 值得注意的是，这个函数只支持xval作为一维数组输入，输出的yval同样是一个数组

x = [0.40, 0.55, 0.65, 0.80, 0.90, 1.05]
fx = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
xval = np.linspace(0.4, 0.9, 100)
table_cs, newton_xishu,  duoxiangshi, yval = Interp_Newton(x, fx, xval)
print(table_cs)
print(newton_xishu)
print(duoxiangshi)
print(yval)
plt.figure(1)
plt.scatter(x, fx)
plt.plot(xval, yval, '-r')
plt.xlabel(r'$x$')
plt.ylabel(r"$f(x)$")
plt.legend(['real_value', 'fitted_value'])
plt.savefig('exercise-04.jpg', dpi=300, bbox_inches='tight')
plt.show()