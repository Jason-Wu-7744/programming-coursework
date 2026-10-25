# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

plt.figure(1)
x = np.arange(0, 50.01, 0.01)
y1 = x
y2 = np.e**x
y3 = np.log10(x)
y4 = np.log(x)

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.subplot(2, 2, 4)
plt.plot(x, y4)

plt.savefig('exercise-01.jpg', dpi=600, bbox_inches='tight')
plt.show()