# import math
# import random
#
# print(math.pi, math.log2(5), math.log(10))
# for _ in range(20):
#     print(random.randint(1, 30))
#
# stores = ['Mos', '7-11', 'Fami', 'Starbucks']
# for _ in range(20):
#     print(random.choice(stores))
#
# cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
#
# for _ in range(5):
#     random.shuffle(cards)
#     print(cards)
import itertools

teams = ['A', 'B', 'C', 'D', 'E', 'F']
p1 = list(itertools.permutations(teams, 2))
print(type(p1))
print(len(p1), p1)
c1 = list(itertools.combinations(teams, 2))
print(type(c1), len(c1))
print(c1)
