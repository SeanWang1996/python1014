d1 = {'name': 'poop', 'duration': 35}
d2 = dict(name='poop', duration=35)
d3 = dict([('name', 'poop'), ('duration', 35)])
print(type(d1), type(d2), type(d3))
print(d1, d2, d3)
print(d1 == d2, d1 == d3)
for k1 in d1:
    print(f'[iteration1]key={k1}, value={d1[k1]}')
for k2 in d1.keys():
    print(f'[iteration2]key={k2}, value={d1[k2]}')
for value in d1.values():
    print(f"value={value}")
for kx, vx in d1.items():
    print(f'[iteration3]key={kx}, value={vx}')