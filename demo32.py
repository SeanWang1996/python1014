from decimal import Decimal as Dec
c1 = 5 + 4j
c2 = 3 - 7j

print(c1 + c2, c1 - c2, c1 * c2, c1 / c2)
print(c1 ** 2)
print(c1.real, c1.imag, (c1.real ** 2 + c1.imag ** 2) ** 0.5)
print(abs(c1))
print(abs(c2))
print((-1) ** 0.5)

print(2**512)

print(Dec(2.968))
print(Dec('2.968'))
print(Dec(2.968)-Dec(2968)*Dec('0.001'))
print(Dec('2.968')-Dec(2968)*Dec('0.001'))