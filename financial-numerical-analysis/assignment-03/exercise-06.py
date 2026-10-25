# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np

normal = np.random.randn(50, 50)
print(normal)

normal = np.delete(normal, 9, 0)
normal = np.delete(normal, 24, 0)
# print(normal.shape)
normal = np.delete(normal, 17, 1)
normal = np.delete(normal, 43, 1)

