# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

x = np.arange(0, 10.1, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
ax1 = plt.axes([.2, .2, .7, .7])
plt.plot(x, y1, '+')
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")

ax2 = ax1.twinx()
plt.plot(x, y2, '*')
# plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
#两边都需要命名坐标轴

plt.text(2.5, 0.7, r'$sin(x)$')
plt.text(0.5, -0.8, r'$cos(x)$')

plt.savefig('exercise-03.jpg', dpi=600, bbox_inches='tight')
plt.show()