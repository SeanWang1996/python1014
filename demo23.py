d1 = {'name': 'Poop', 'duration': 35}
d2 = {'duration': 35, 'name': 'Poop'}
print(d1, d2, d1 == d2, d1 is d2)
print(d1['name'], d2['duration'])
# print(d1['xyz'])
print('xyz' in d1, 'name' in d1)
k1 = 'duration'
print(k1 in d1 and d1[k1])

A1 = True
A2 = False
BS = [True, False, 100, 3.14, 5+4j, None, "hello world"]

for b in BS:
    print(A1 and b)

for b in BS:
    print(A2 and b)