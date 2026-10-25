# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

def integral_fun(x):
    f = np.sqrt(1 + np.e**x)
    return f

def integral_trapezoid(a, b, n):
    x_0 = a
    x_n = b
    h = (x_n - x_0)/n
    xp = np.arange(x_0, x_n+h, h)
    fxp = integral_fun(xp)
    fxp[0] = fxp[0]/2
    fxp[-1] = fxp[-1]/2
    Tn = np.sum(fxp)*h
    return Tn

n_list = [2, 4, 8, 16, 32, 64, 128, 256, 512]

# print("n\tT(f)\tError\tRatio")
print(f"{'n':<4}\t{'T(f)':<18}\t{'Error':<18}\t{'Ratio':<18}")
for i in range(len(n_list)):
    error = 4.006994 - integral_trapezoid(0, 2, n_list[i])
    if i == 0:
        print(f"{n_list[i]:<4}\t{integral_trapezoid(0, 2, n_list[i]):<18.4f}\t{error:<18.8f}")
    else:
        ratio = (4.006994 - integral_trapezoid(0, 2, n_list[i-1]))/error
        # print('n取', n_list[i], '时，误差为', error)
        # print(n_list[i], integral_trapezoid(0, 2, n_list[i]), error, ratio)
        print(f"{n_list[i]:<4}\t{integral_trapezoid(0, 2, n_list[i]):<18.4f}\t{error:<18.8f}\t{ratio:<18.4f}")

# 复合梯形法中，n每扩大一倍，误差就变为原来的四分之一