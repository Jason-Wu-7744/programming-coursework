# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

# 判断两个迭代公式是否收敛
def g_equation_1_diff(a):
    g_diff = 1/3*(0.8 + a**2)**(-2/3)*2*a
    return g_diff
print(g_equation_1_diff(1.5))

if np.abs(g_equation_1_diff(1.5)) < 1:
    print("迭代法1收敛于1.5")
else:
    print("迭代法1不收敛")

def g_equation_2_diff(a):
    g_diff = 1/2*(a**3 - 0.8)**(-1/2)*3*a**2
    return g_diff
print(g_equation_2_diff(1.5))

if np.abs(g_equation_2_diff(1.5)) < 1:
    print("迭代法2收敛于1.5")
else:
    print("迭代法2不收敛")

#可以得出迭代法1收敛更快
# 使用Aitken算法
def g_equation_1(a):
    g = (0.8 + a**2)**(1/3)
    return g

x0 = 1.5
x1 = g_equation_1(x0)
x2 = g_equation_1(x1)
rho2 = (x2 - x1)/(x1 - x0)
err = rho2/(1-rho2)*(x2 - x1)
x3 = x2 + err
print(err)

while np.abs(err) >= 10**(-5):
    print(1)
    x0 = x3
    x1 = g_equation_1(x0)
    x2 = g_equation_1(x1)
    rho2 = (x2 - x1) / (x1 - x0)
    err = rho2 / (1 - rho2) * (x2 - x1)
    x3 = x2 + err

print("近似根为", x3)