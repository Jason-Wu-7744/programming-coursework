# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

data = pd.read_excel('least_squares_points.xlsx')
print(data)

plt.figure(1)
plt.scatter(data['xi'], data['yi'])
# plt.show()

n = len(data['xi'])
sum_x = np.sum(data['xi'])
sum_y = np.sum(data['yi'])
print(sum_x, sum_y, n)

sum_x_square = 0
for a in data['xi']:
    sum_x_square += a**2
print(sum_x_square)

sum_xy = 0
for i in range(len(data['xi'])):
    sum_xy += data.iloc[i, 0]*data.iloc[i, 1]
print(sum_xy)

A = np.array([[n, sum_x], [sum_x, sum_x_square]])
print(A)
b = np.array([[sum_y], [sum_xy]])
print(b)

x = np.dot(np.linalg.inv(A), b)
print(x)

print("斜率：", x[1, 0])
print("截距", x[0, 0])

x_plot = np.arange(-1, 1.1, 0.0001)
y_plot = x[1, 0]*x_plot + x[0, 0]
plt.plot(x_plot, y_plot, "-r")
plt.legend(['real value', 'fitted value'])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.savefig('exercise-03.jpg', dpi=600, bbox_inches='tight')
plt.show()

SSR = 0
for i in range(n):
    SSR += (x[1, 0]*data.iloc[i, 0] + x[0, 0] - data.iloc[i, 1])**2
E = np.sqrt(SSR/n)
print("最小二乘拟合的均方根误差为", E)