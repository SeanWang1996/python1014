l1 = ['A', 'B']
print(hex(id(l1)))
l1 += ['C', 'D']
print(hex(id(l1)))
print([l for l in l1])

s1 = "AB"
print(hex(id(s1)))
s1 += "CD"
print(hex(id(s1)))
print([l for l in s1])