# l1 = []
# l2 = list()
# l3 = [1, 2, 3]
# l4 = ['a', 2, 3]
# l5 = [500, None, ['p', 'q']]
# print(type(l1), type(l2), type(l3), type(l4), type(l5))
# l6 = list('PQRST')
# print(l6)
# for x in l6:
#     print(x)
# print(l3 == l4)
# l7 = [1, 2, 3]
# print(l3 == l7)
# print(l3 is l7)
# print(l6[0], l6[4], l6[-1], l6[-5])
# # print(l6[5])
# # print(l6[-6])
# print(l6[int(0.1)])
# l1 = list('ABCDEFG')
# l1 *= 2
# l2 = 2 * l1
# print(l1)
# print(l2)
# print(l1[2:5])
# print(l2[:10], l2[10:])
# print(l1[0:10:2])
# print(l2[::3])
# print("reverse order")
# print(l1[-5:-2], l1[-2:-5])
# print(l1[-2:-5:-1])
# print(l1[::-1])
# print(l1[-2:-5])
#
# l1 = ['A', 'B']
# print(hex(id(l1)))
# l1 += ['C']
# print(l1, hex(id(l1)))
#
#
# l2 = ['A', 'B']
# print(hex(id(l2)))
# l2.append('C')
# print(l2,hex(id(l2)))
#
# l3 = ['A', 'B']
# print(hex(id(l3)))
# l3.extend('C')
# print(l3,hex(id(l3)))

# l1 = ['A', 'B']
# print(hex(id(l1)))
# l1 += ['C', 'D', 'E', 'F', 'G']
# l1 += ['C', 'D', 'E', 'F', 'G']
# print(l1, hex(id(l1)))
#
# l2 = ['A', 'B']
# print(hex(id(l2)))
# l2.append(['C', 'D', 'E', 'F', 'G'])
# l2.append(['C', 'D', 'E', 'F', 'G'])
# print(hex(id(l2)))
#
# print(l2)
# l3 = ['A', 'B']
# print(hex(id(l3)))
# l3.extend(['C', 'D', 'E', 'F', 'G'])
# l3.extend(['C', 'D', 'E', 'F', 'G'])
# print(hex(id(l3)))
# print(l3)
# l1 = ['A', 'B', 'C', 'D']
# for l in l1:
#     print(l)
# l2 = ['Apple', 'Banana', 'Cookie', 'Donut']
# for l in l2:
#     print(l)
# print([l * 30 for l in l1])
# print([l for l in l2 if len(l) < 6])
# print('X' in l1, 'D' in l1)
# print('Apple' in l2, 'apple' in l2)

l1 = list('UIOYTTUIWYEUQIWYEIUWQTEQWOTU') * 3
print(l1)
print(len(l1), l1.count('U'))
print(l1.count('X'))
print(hex(id(l1)))
l1.sort()
print(hex(id(l1)))
print(l1)
l1.sort(reverse=True)
print(hex(id(l1)))
print(l1)
l2 =list('qwertQWERTYUIOPyuiop')
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
l2.sort(key=str.lower)
print(l2)