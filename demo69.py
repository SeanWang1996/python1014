# import pandas as pd
# import numpy as np
#
# pd1 = pd.DataFrame(np.random.randn(6, 7),
#                    index=list(range(0, 12, 2)),
#                    columns=list(range(0, 7, 1)))
# print(pd1)
#
#
# def myFunc(x):
#     return x.max() - x.min()
#
#
# func1 = lambda x: x.max() - x.min()
# # print(pd1.apply(func1))
# print('-------')
# print(pd1.apply(myFunc))
# print('-------')
# print(pd1.apply(myFunc, axis=1))
# print('-------')
# print(pd1.apply(myFunc, axis='columns'))
# print('-------')
# print('-------')
# func2 = lambda x: pd.Series([x.min(), x.max()], index=['min', 'max'])
# print('-------')
# print(pd1.apply(func2))
# print('-------')
# print(pd1.apply(func2, axis=1))