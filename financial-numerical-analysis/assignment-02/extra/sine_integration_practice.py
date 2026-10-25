# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import numpy as np

s = 0
for i in np.arange(0, np.pi/2, 0.001):
    delta = np.sin(i)*0.001
    s += delta

print(s)