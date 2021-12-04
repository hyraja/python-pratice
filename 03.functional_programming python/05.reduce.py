# Reduce()
# reduce is not come with python builtins you need to import from functools module.
# reduce allow us to reduce something.
# it reduce things from left to right means lower to high.
# syntax---> reduce(function,iterable_items,initial_item_of_iterable)

from functools import reduce
my_list = [1, 2, 3]

def accumulator(acc, item):
    print(acc, item)
    '''0 1
       1 2
       3 3 '''
    return acc+item


print(reduce(accumulator, my_list, 0))
''' it 1st take acc=0 then it combine with
                                          acc+item=>1 so..... 0 1---> our itearable items in my_list
                                                         then 1 2---> our itearable items in my_list
                                                         then 3 3---> our itearable items in my_list
                                                         then 3+3 = 6 so reduce directly
                                                        gives us answer as 6 '''

print(my_list)
