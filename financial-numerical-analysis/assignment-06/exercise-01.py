# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt

#画图找初始区间
x = np.arange(-10, 10)
fx = x - 3/(1+x**4)
# print(fx)
plt.figure(1)
plt.axis([-5, 5, -5, 5])
plt.plot(x, fx)
# plt.show()

#定义函数
def equation(m):
    fm = m - 3/(1+m**4)
    return fm

#二分法算法
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

print("[0, 2]内的α为：", rootfinding_bisection(0, 2, 5*10**(-8)))