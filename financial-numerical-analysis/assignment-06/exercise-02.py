# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt

def equation(m):
    fm = m**4 - 5.4*m**3 + 10.56*m**2 - 8.954*m + 2.7951
    return fm

def equation_diff(m):
    dfm = 4*m**3 - 16.2*m**2 + 21.12*m - 8.954
    return dfm

#画图
x = np.arange(1, 1.2001, 0.0001)
y = equation(x)

plt.figure(1)
plt.plot(x, y)
# plt.show()

def rootfinding_newton(x0, e):
    f = equation(x0)
    df = equation_diff(x0)
    x1 = x0 - f/df
    while abs(x1-x0) > e:
        x0 = x1
        f = equation(x0)
        df = equation_diff(x0)
        x1 = x0 - f / df
    return x1

# print(rootfinding_newton(1, 10**(-8)))
# print(rootfinding_newton(1.2, 10**(-8)))
#出现了分母为0的报错， 这是一个病态求根重根问题，由于1.1这个三重跟导致的收敛速度慢和不确定区间导致的，只能放大误差容限

print(rootfinding_newton(1, 10**(-5)))
print(rootfinding_newton(1.2, 10**(-5)))
#算出了两个相近的根
