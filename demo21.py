import copy

l1 = list('QWERTYUIOP')
l2 = l1
l3 = list(l1)
l4 = l1[:]
l5 = copy.copy(l1)
print(l1, l2, l3, l4, l5)
l1[0] = 'q'
l2[1] = 'w'
print(l1, l2, l3, l4, l5)
print(hex(id(l1)))
print(hex(id(l2)))
print(hex(id(l3)))
print(hex(id(l4)))
print(hex(id(l5)))