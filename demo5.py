# x0 = 2 ^ 512
# x1 = 2 ** 512
# x2 = 3.14
# x3 = 5 + 4j
# x4 = 'hello'
# x5 = "world"
# x6 = b'''welcome'''
# x7 = True
# x8 = False
# x9 = None
# print(x0)
# print(type(x1), x1, sep="||")
# print(type(x2), x2)
# print(type(x3), x3)
# print(type(x4), x4)
# print(type(x5), x5)
# print(type(x6), x6)
# print(type(x7), x7)
# print(type(x8), x8)
# print(type(x9), x9)
#
# x1= 300
# print("x1 in dec={0}, in bin={0:b}, in oct={0:o}, in hex={0:x}".format(x1))
# print(0b100100100)
# print(0o100)
# print(0x10)
# x2= 512
# print("x2={0:b}".format(x2))
# # divide
# print(5 / 2, 5 / 3, 5 / 4)
# print(5 // 2, 5 // 3, 5 // 4)
# print(5 % 2, 5 % 3, 5 % 4)
# print(round(1.5), round(2.5), round(3.5), round(4.5))
# print(round(1.4), round(2.4), round(3.4), round(4.4))
# print(round(1.6), round(2.6), round(3.6), round(4.6))
# import ast
#
# x1 = "None"
# x2 = None
# print(x1 == x2, type(x1), type(x2))
# y1 = "None"
# y2 = "None"
# # y3 = "None"
# y3 = "3+5"
# z1 = ast.literal_eval(y1)
# print(z1, type(z1))
# z2 = None if y2 == "None" else y2
# print(z2, type(z2))
# z3 = eval(y3)
# print(z3, type(z3))
# print(z1 == z2, z1 == z3, z2 == z3)
# print(z1 is z2, z1 is z3, z2 is z3)
# x = 5
# print(x)
# # print(y=6)
# print(y := 6)

# inputs = list()
# message1 = "write something from user:"
#
# while (current := input(message1)) != "quit":
#     inputs.append(current)
# print("result = {}".format(inputs))

# x = 5
# print(x, hex(id(x)))
# x = 6
# print(x, hex(id(x)))
# y = [5]
# print(y, hex(id(y)), hex(id(y[0])))
# y[0] = 6
# print(y, hex(id(y)), hex(id(y[0])))

l1 = ['apple', 'banana', 'cookie']
l2 = ['apple', 'banana', 'cookie']
l3 = l1


print(hex(id(l1)))
print(hex(id(l2)))
print(hex(id(l3)))
print(l1 == l2, l1 == l3)
print(l1 is l2, l1 is l3)