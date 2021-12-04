# MAP function

# map allow us to simplify our code and also gives return as
# map object, if you want to see the answer u need to convet it into list.

# syntax: ---->>> map(function, iterable_items_for_function)


# print out multiply of 2 with all element

# map gives us result as multiply 2 with all element and also loop through all elements

def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3])))  # [2,4,6]
''' map automatically call the function and also loop through all
the item , we just provide the name of the function '''


my_list = [1, 2, 3]


def multiplyby2(item):
    return item*2


print(list(map(multiplyby2, my_list)))  # [2,4,6]
print(my_list)  # [1,2,3]

''' a true function i.e map doesnot affect outside world. 
 so thats why it creates another list for the result as [2,4,6]
 and don't affect the previous list like [1,2,3] as result . '''
