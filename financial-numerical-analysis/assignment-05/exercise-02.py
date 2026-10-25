# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
import numpy as np
import pandas as pd

#第一小题
data = pd.read_excel('homework5_2_1.xlsx', index_col=0)
print(data)

data_first5 = data.iloc[0:5, :]
print(data_first5)
data_last5 = data.iloc[-5:, :]
print(data_last5)
print(data.describe())

#第二小题
data_first5.to_excel('homework5_2_2.xlsx')

#第三小题
data_last5.to_csv('homework5_2_3.csv')

#第四小题
data.describe().to_string('homework5_2_4.txt')
