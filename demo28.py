
items = ['S', 'S', 'M', 'L', 'S', 'M', 'L', 'S', 'M', 'L', 'M', 'L', 'S', 'M', 'SS', 'SS', 'XL', 'XL']

totalSales = {}
# totalSales = {'S': 0, "M": 0, "L": 0}
print(type(totalSales))
for item in items:
    totalSales.setdefault(item, 0)
    totalSales[item] += 1
print(totalSales)