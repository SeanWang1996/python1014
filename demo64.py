import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slides': [200, 250, 230, 300]}
print(data)
df1 = pd.DataFrame(data)
print(df1)
print(type(df1), type(data))
print(df1.head(2))
print(df1.index)
print(df1.columns)
# create more attributes
df2 = pd.DataFrame(data, index=['p1', 'p2', 'p3', 'p4'],
                   columns=['course', 'slides', 'year', 'instructor'])
print(df2)
print(df2.columns)
print(df2.index)
print("---sampling dataframe---")
v1 = df2['course']
print(type(v1))
print(v1)
v2 = df2[['course', 'year']]
print(type(v2))
print(v2)
v3 = df2.loc['p1']
print(type(v3))
print(v3)
v4 = df2.loc[['p1', 'p2']]
print(type(v4))
print(v4)
df2['instructor'] = 'MarkHo'
print(df2)
df2['instructor'] = ['Frank', 'Ken', 'Mark', 'Tom']
print(df2)