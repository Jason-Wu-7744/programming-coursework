# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt

def equation(m):
    fm = m**3 + 2*m**2 + 10*m - 20
    return fm

x = np.arange(1.3, 1.5, 0.001)
y = equation(x)
plt.figure(1)
plt.plot(x, y)
# plt.show()

def rootfinding_secant(x0, x1, e):
    f0 = equation(x0)
    f1 = equation(x1)
    x2 = x1 - f1/((f1-f0)/(x1-x0))
    f2 = equation(x2)
    while abs(x2 - x1) > e:
        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f2
        x2 = x1 - f1/((f1-f0)/(x1-x0))
        f2 = equation(x2)
    return x2

print(rootfinding_secant(-1, 3, 10**(-6)))
print(rootfinding_secant(1.7, 1.5, 10**(-6)))
