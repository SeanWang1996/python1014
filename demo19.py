v1 = []
v2 = ()
v3 = {}
v4 = set()
print(type(v1), type(v2), type(v3), type(v4))
v5 = ['k']
v6 = ('k',)
v7 = {'k'}
v8 = set('k')
v9 = {'k': 'k'}
print(type(v5), type(v6), type(v7), type(v8), type(v9))
t1 = ('A', 'B', 'C', 1, 2, 3)
print([t for t in t1])
t2 = ('A', 'B')
print(hex(id(t2)))
t2 += ('C', 'D')
print(hex(id(t2)))
a1 = 5
a2 = 3
print(a1, a2)
t = a1
a1 = a2
a2 = t
print(a1, a2)
a3 = 5
a4 = 3
print(a3, a4)
a3, a4 = a4, a3
print(a3, a4)
a5 = "hello world"
a6 = 3 + 4j
print(a5, a6)
a5, a6 = a6, a5\
# a5 = a6
# a6=a5
print(a5, a6)
c1 = 'A'
c2 = 'K'
c3 = 'Q'
c4 = 'J'
c5 = 10
print(c1, c2, c3, c4, c5)
c1, c3, c5, c2, c4 = c1, c2, c3, c4, c5
print(c1, c2, c3, c4, c5)
v1, v2, v3 = ['Mark', 'Frank', 'James']
print(v1, v3, v2)