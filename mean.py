import pandas as pd
columns = pd.read_csv('columns1.csv')
a = columns.head()
print(a.mean(axis=1))

