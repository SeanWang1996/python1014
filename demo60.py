import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz': 28, 'testit': 14}
print(type(d1))
s1 = pd.Series(d1)
print(type(s1))
print(s1)
print(s1.index)
print(s1.values)
print('poop' in d1, 'c#' in d1, 'poop' in s1, 'c#' in s1)
l1 = ['andbiz2', 'testit', 'anbiz', 'anbiz3', 'bdpy']
s2 = pd.Series(d1, index=l1)
print('-------')
print(s2)
print('-------')
s3 = pd.Series(d1, index=['andbiz', 'testit', 'poop', 'bdpy'])
print(s3)
print("is Nan::")
print(pd.isna(s2))
print(s2.isna())
print("is Null:")
print(pd.isnull(s2))
print(s2.isnull())
d2 = {'poop':'Mark','bdpy':None,'andbiz2':None,'testit':'Frank','andbiz3':'Tim'}
s4 = pd.Series(d2, index=l1)
print('---a little bit more confusing----')
print(s4)
print(s4.isnull())
print(s4.isna())