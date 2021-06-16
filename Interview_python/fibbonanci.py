# find out fibbonanci of given number

# method 1 (using generator)
def fib(num):
    a, b = 0, 1
    for i in range(num):
        #print('i value', i)
        yield a
        a, b = b, a+b


for x in fib(5):
    print(f' fibbonaci {x}')


# method 2 (using while)

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


# fib(5)
