import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

bin_plt = np.linspace(-0.098, 0.098, 100)
norm_plt = norm.pdf(bin_plt, loc=4.99979025261974, scale=34.4530584272356)
plt.semilogy(bin_plt, norm_plt)
plt.figure(1)
plt.plot(bin_plt, norm_plt)
plt.show()