# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.family": "STIXGeneral",
                      "font.size": 20,
                      "mathtext.fontset": "cm"})

x = np.arange(0.01, np.pi + 0.01, 0.01)
y = np.sin(x)**x
plt.plot(x, y)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.title(r'$sin(x)^x$')

plt.savefig('exercise-02.jpg', dpi=600, bbox_inches='tight')
plt.show()