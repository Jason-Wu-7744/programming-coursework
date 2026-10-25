# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

for i in range(5, 10, 1):
    x = np.arange(1, i+1.01, 0.01)
    y = 1
    for a in range(i+1):
        y *= (x-(i+1))
    plt.subplot(2, 3, i-4)
    plt.plot(x, y)
    plt.legend([str(i)])
plt.savefig('exercise-03.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 上述图像单调性、凹凸性轮换，可以联合起来用于拟合函数图像。