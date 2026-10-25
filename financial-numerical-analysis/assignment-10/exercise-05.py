# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

# 第一小问（二分法）
def equation(r):
    fr = 5361.74*(1+r)**6-924.56*(1+r)**5-924.56*(1+r)**4-924.56*(1+r)**3-924.56*(1+r)**2-924.56*(1+r)-924.56*(1+r)
    return fr

def rootfinding_bisection(a, b, e):
    c = (a+b)/2
    while b-c > e:
        sign_fa = np.sign(equation(a))
        sign_fb = np.sign(equation(b))
        sign_fc = np.sign(equation(c))
        if sign_fb*sign_fc <= 0:
            #这里不写=似乎影响不大
            a = c
        else:
            b = c
        c = (a + b) / 2
    return c

# 画图找左右端点
# plt.figure(1)
# x = np.linspace(0, 0.025, 100)
# y = equation(x)
# plt.plot(x, y)
# plt.show()

print('二分法求出的月利率r是', rootfinding_bisection(0, 0.02, 10**(-6)))

# 第二小问（牛顿插值）
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

fx = [0.0025, 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175]
x = []
for i in range(len(fx)):
    x.append(equation(fx[i]))
xval = np.array([0])
a, b, c, d = Interp_Newton(x, fx, xval)
print('差商表为：\n', a)
print('牛顿法求出的月利率r是', d[0])

plt.figure(1)
plt.scatter(fx, x)
x_show = np.linspace(0, 0.02, 100)
y_show = Interp_Newton(fx, x, x_show)[3]
plt.plot(x_show, y_show, '-r')
plt.legend(['real_value', 'fitted_value'])
plt.xlabel(r'$r$')
plt.ylabel(r'$NPV$')
plt.savefig('exercise-05.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 第三小问
print("牛顿插值法解的误差为：", rootfinding_bisection(0, 0.02, 10**(-6)) - d[0])