from pandas import Series

list1 = [3, 1, 4, 5, 9, 6, 87, 100]
series1 = Series(list1)
print(type(list1), type(series1))
print(series1)
print(series1.index)
print(series1.values)
series2 = Series([4, 7, -5, 3], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
print(series2)
print(series1[0], series1[7])
# print(series1[-1])
# print(series1[8])
# print(series1[[0, 2, 4, 6, 8]])
print(series2['nangang'], series2['banqiao'])
print(series2[series2 > 0])
print(series1 ** 2)
print(series2[series2 > 0] * 3 + 2)
print(series2[['nangang', 'taipei', 'banqiao']])
print(series1[[7, 5, 3, 1]])
print('-----')
print(type(series1[0]), series1[0])
print(series1[[0, 1, 2]]), '\n',type(series1[[0, 1, 2]])
print(series2['nangang'])
print(series2[['nangang', 'taipei']])
print(type(series2[['nangang', 'taipei']].values), series2[['nangang', 'taipei']].values)