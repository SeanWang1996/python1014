fruits = ['Apple', 'Banana']
print(hex(id(fruits)))


def addFruit(parameter):
    print(hex(id(parameter)))
    parameter.append('Cooke')


print(fruits)
addFruit(fruits)
print(hex(id(fruits)))
print(fruits)

p = 10


def addTen():
    print("p=", p)
    #p+=10
addTen()