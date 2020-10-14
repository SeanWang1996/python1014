def demo34(x, y, z, *t):
    print(f'first variable={x}, second variable={y}, third variable={z}')
    print([element for element in t])


demo34("Hi", "Hello", "World")
demo34(x=5, y=7, z=9)
demo34(z=9, x=5, y=7)
demo34(5, 7, z=9)
demo34(5, 7, 9, 100)
demo34(5, 7, 9, 100, 200, 300)
l1 = ['apple', 'banana', 'cookie']
demo34(1,2,3,l1)
demo34(1,2,3,*l1)