# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
# Alternative/practice version; the label does not imply original research.
import pandas as pd
import numpy as np

# data4 = pd.DataFrame(np.random.rand(3, 2), columns=['col1', 'col2'], index=['a', 'b', 'c'])
# print(data4)

# data1 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# data2 = pd.Series(np.random.rand(4), index=['a', 'b', 'c', 'd'])
# print(data1)
# print(data2)

# data3 = pd.DataFrame([[0.25, 0.5, 0.75, 1.0], [4, 5, 6, 7]])
# data4 = pd.DataFrame(np.random.rand(3, 2), columns=['col1', 'col2'], index=['a', 'b', 'c'])
# print(data3)
# print(data4)

# population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135}
# population = pd.Series(population_dict)
# print(population, population.shape)

# data5 = pd.DataFrame({'a':[1, 2, 3], 'b':[1, 4, 9]})
# print(data5, data5.ndim)

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data[['a', 'c']])