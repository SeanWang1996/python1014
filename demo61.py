import pandas as pd

c1 = pd.Series([1000, 800, 500, 300], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
c2 = pd.Series([500, 300, 400], index=['hsinchu', 'taichung', 'tainan'])
c3 = pd.Series([2000, 1800, 300, 800], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
c4 = pd.Series([2500, 1300, 1400], index=['hsinchu', 'taichung', 'tainan'])
print(c1 + c2)
print('--same index can be added--')
print(c1+c3)
print('--different index need to be merged, but with care..--')
merge1 = c1.append(c2)
print(merge1)
merge2 = c3.append(c4)
print(merge2)
merge_all = merge1 + merge2
print(merge_all)
print('about index')
merge_all.index=['taipei','taichung','tainan','nangang','hsinchu','taoyuan','banqiao']
print(merge_all)
merge_all.index=['sta1','sta2','sta3','sta4','sta5','sta6','sta7']
print(merge_all)