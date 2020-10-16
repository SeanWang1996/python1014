import pandas as pd
import numpy as np

pd1 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(pd1)
print(pd1[:])
print(pd1[:2])
print(pd1[2:])
print('----using iloc----')
print(pd1.iloc[:2])
print(pd1.iloc[2:])
print('---using iloc vertically---')
print(pd1.iloc[:, :2])
print(pd1.iloc[:, 2:])
print(pd1.iloc[1:3, 2:4])
print(pd1.iloc[1, 2])