# *args and **kwargs
# we use *args for giving multiple positional argument using single parameter and
# you also give the name to parameter as your wish
# we use **kwargs for giving multiple keyword arguments to the functions.


def sup_fun(*args, **kwargs):
    print(args)  # (1, 2, 3, 4, 5, 6) i.e ---> args store in this function as tuple
    # {'num1': 1, 'num': 200} i.e ----> kwargs store in this fuction as a dictionary
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(sup_fun(1, 2, 3, 4, 5, 6, num1=1, num=200))

# Rules : params, *args, default parameters, **kwargs
# ------------------------------------------------------

# ex:


def super(name, *args, age=30, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super('raja', 1, 2, 3, 4, 5, 6, num1=1, num=200))


# ---------------------------------------------------
# question to find the highest even number from the list
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Q2 find out max number without using max() function


def max(a):

    res = a[0]
    for i in a:
        if i > res:
            res = i
    return res


array = [1, 2, 3, 4, 5, 6]

print(max(array))
