# # import pandas as pd
# # import numpy as np
# #
# # s1 = pd.Series(range(5), index=['p', 'q', 'r', 's', 't'])
# # print(s1)
# # print(s1.index)
# # index1 = pd.Index(['C', 'D', 'E', 'F', 'G', 'J'], dtype='object')
# # print(type(index1), index1)
# # print(index1[2:], index1[:2])
# # i1 = pd.Index(np.arange(3))
# # i2 = list(np.arange(3))
# # print(i1)
# # print(i2)
# # data = ['Nangang', 'Taipei', 'Banqiao']
# # pd1 = pd.Series(data, index=i1)
# # print(pd1)
# # pd2 = pd.Series(data, index=i2)
# # print(pd2)
# # print(2 in i1, 2 in i2, 2 in pd1, 2 in pd2)
# # i3 = pd.Index(['Taipei', 'Taipei', 'Taipei'])
# # pd3 = pd.Series(data, index=i3)
# # print(pd3)
# # print('-----')
# # print(pd3['Taipei'])
# import pandas as pd
# import numpy
#
# s1 = pd.Series([20, 15, 18, 37, 25], index=['mar', 'jan', 'feb', 'may', 'apr'])
# s2 = s1.reindex(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'])
# print(s2)
# s3 = pd.Series(['L', 'M', 'S'], index=[0, 5, 10])
# print(s3)
# s4 = s3.reindex(range(15), method='ffill')
# print(s4)
# s5 = pd.DataFrame(numpy.arange(16).reshape(4, 4), index=[1, 2, 3, 4],
#                   columns=['kotlin', 'swift', 'c++', 'java'])
# print(s5)
# s6 = s5.reindex(columns=['c++', 'swift', 'java', 'kotlin'])
# print(s6)
import pandas as pd

dict1 = {'station': ['nangang', 'taipei', 'banqiao', 'taoyuan', 'hsinchu'],
         'order': [0, 1, 2, 3, 4],
         'backorder': [5, 4, 3, 2, 1]}
pd1 = pd.DataFrame(dict1)
print(pd1)
print(pd1.drop(2))
print(pd1.drop([1, 3]))
print(pd1.drop('order', axis=1))
print(pd1.drop(['order', 'backorder'], axis=1))
print(pd1.drop(['order', 'backorder'], axis='columns'))
pd1.drop([1, 2, 4], inplace=True)
print(pd1)
