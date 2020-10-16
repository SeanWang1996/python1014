# import pandas as pd
#
# data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
#         'year': [2018, 2017, 2019, 2020],
#         'slides': [200, 250, 230, 300]}
# print(data)
# df1 = pd.DataFrame(data)
#
# s1 = pd.Series(['taipei', 'hsinchu', 'taichung', 'kaohsiung'],
#                index=[0, 1, 2, 3])
# print('----------------------------')
# df1['location'] = s1
# print(df1)
# print('----------------------------')
# s2 = pd.Series(['remote', 'local'], index=[0, 3])
# df1['method'] = s2
# print(df1)
# print('----------------------------')
# df1['heavy'] = df1['slides'] > 250
#
# print(df1)
# print('----------------------------')
# del df1['slides']
# print(df1)
import pandas as pd

data = {'poop': {2019: 5, 2020: 8},
        'bdpy': {2018: 5, 2019: 7, 2020: 10}}
df1 = pd.DataFrame(data)
print(df1)
df2 = df1.T
print(df2)
df3 = pd.DataFrame(data, index=[2018, 2019, 2020])
print(df3)