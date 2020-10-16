import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slides': [200, 250, 230, 300]}
print(data)
df1 = pd.DataFrame(data)
print(df1)
print(type(df1), type(data))
print(df1.head(2))
print('----------------------------')
print(df1.index)
print(df1.columns)
print('----------------------------')
# create more attributes
df2 = pd.DataFrame(data, index=['p1', 'p2', 'p3', 'p4'],
                   columns=['course', 'slides', 'year', 'instructor'])
print(df2)
print(df2.columns)
print(df2.index)