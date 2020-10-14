numbers = [6, 5, 3, 8, 4, 2, 5, 11, 9]

sum = 0

for n in numbers:
    sum += n
print(f"total={sum}")

numbers2 = [6, -5, 3, -8, 4, -2, 5, -11, 9]
for n in numbers2:
    if n < 0:
        numbers2.remove(n)
print(numbers2)

numbers3 = [6, -5, 3, -8, 4, -2, 5, -11, 9]
for n in numbers3[:]:
    if n < 0:
        numbers3.insert(0, n)
print(numbers3)