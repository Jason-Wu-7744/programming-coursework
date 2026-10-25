import numpy as np
import pandas as pd

data_1 = pd.read_excel("RESSET_DRESSTK_1990_2000_1.xlsx")
data_2 = pd.read_excel("RESSET_DRESSTK_2001_2010_1.xlsx")
data_3 = pd.read_excel("RESSET_DRESSTK_2011_2015_1.xlsx")
data_4 = pd.read_excel("RESSET_DRESSTK_2016_2020_1.xlsx")
data = pd.concat([data_1, data_2, data_3, data_4], axis=0)
print(data)
data.columns = ['date', 'close']
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values('date').reset_index(drop=True)
print(data)

data.to_csv("data_000858.csv", index=False)