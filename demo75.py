# import numpy as np
# import pandas as pd
# from pandas_datareader import wb
#
# s1 = pd.Series([1, 1, 2, 3, 4, 5, 8, 10])
# print(s1)
# print(s1.pct_change())
#
# data = wb.download(indicator='SE.PRM.TENR',
#                    country=['all'],
#                    start=2002,
#                    end=2018)
# data2 = data.reset_index()
# france1 = data2[data2.country=='France']
# print(france1['SE.PRM.TENR'])
# print(france1['SE.PRM.TENR'].pct_change())

# import numpy as np
# import pandas as pd
# from pandas_datareader import wb
#
# data = wb.download(indicator='SE.PRM.TENR',
#                    country=['all'],
#                    start=2002,
#                    end=2018)
# data2 = data.reset_index()
# france1 = data2[data2.country == 'France']
# france1.index = france1['year']
# german1 = data2[data2.country == 'Germany']
# german1.index = german1['year']
# print(france1)
# print(german1)
# df1 = pd.DataFrame({'fr': france1['SE.PRM.TENR'], 'de': german1['SE.PRM.TENR']})
# print(df1)

import numpy as np
import pandas as pd
from pandas_datareader import wb

data = wb.download(indicator='SE.PRM.TENR',
                   country=['all'],
                   start=2002,
                   end=2018)
data2 = data.reset_index()
france1 = data2[data2.country == 'France']
france1.index = france1['year']
german1 = data2[data2.country == 'Germany']
german1.index = german1['year']
print(france1)
print(german1)
df1 = pd.DataFrame({'fr': france1['SE.PRM.TENR'], 'de': german1['SE.PRM.TENR']})
print(df1)
print(df1['fr'].corr(df1['de']))
print(df1['fr'].cov(df1['de']))
print(df1.corr())
print(data2.country.value_counts())
print(pd.value_counts(data2.country))
