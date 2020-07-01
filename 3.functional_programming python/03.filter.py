# FILTER fumction

# It filter Things for us.

# syntax:----> filter(function,iterable_items)

my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))  # [1,3]
print(my_list)  # [1,2,3]
''' filter is filtered things for us. and also it doesnot affect
outside if world. so it filter and create another list for only_odd
function and gives [1,3] which is the odd iterables.'''
# as like map  we donot call the whole function, we just need to give function name
#  it automatically call the function in filter .
# filter gives us filtered object which is true or false.
# to display filtered object we use list().
