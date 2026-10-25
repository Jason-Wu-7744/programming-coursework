# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

def integral_fun(x):
    f = np.sqrt(1 + np.e**x)
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

n_list = [2, 4, 8, 16, 32, 64, 128, 256, 512]

print(f"{'n':<4}\t{'T(f)':<18}\t{'Error':<18}\t{'Ratio':<18}")
for i in range(len(n_list)):
    error = 4.006994 - integral_simpson(0, 2, n_list[i])
    if i == 0:
        print(f"{n_list[i]:<4}\t{integral_simpson(0, 2, n_list[i]):<18.4f}\t{error:<18.8f}")
    else:
        ratio = (4.006994 - integral_simpson(0, 2, n_list[i-1]))/error
        print(f"{n_list[i]:<4}\t{integral_simpson(0, 2, n_list[i]):<18.4f}\t{error:<18.8f}\t{ratio:<18.4f}")

# 复合辛普森法中，n每扩大一倍，误差就变为原来的十六分之一
# 相较于复合梯形法，复合辛普森法收敛得更快

# 值得注意的是，就算代入的n是奇数，这段代码函数依然能算出一个结果，但理论上复合辛普森法的n只能是偶数
