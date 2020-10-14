import sys


def fib1(n):
    a, b = 0, 1
    # ctrl+alt+L
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print('')


fib1(100)
# fib1(sys.argv[1])
# fib1(int(sys.argv[1]))
# print('program finished')
