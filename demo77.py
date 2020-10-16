import pandas

from matplotlib import pyplot, rc
print(pyplot.style.available)
data = pandas.read_csv('data/demo67.csv', skiprows=4,index_col="Country Name")
print(data.shape)
# pip install openpyxl
#data.to_excel('data/demo67_output.xlsx', sheet_name='pandas_generated')
ausData = data[data['Country Code']=='AUS']
print(type(ausData))
print(ausData)
print(ausData['1960'])
pyplot.style.use('seaborn-whitegrid')
selected_years = ['1960','1970','1980','1990']
ausData.plot(kind='bar',y=selected_years)
pyplot.show()