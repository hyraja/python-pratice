# fibonanci number using decorator


def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        temp = a
        a, b = b, a+b


for x in fib(21):
    print(x)
'''
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765 '''
''' mindit it is not saving the data in memory '''
