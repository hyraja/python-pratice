# lambda expression

# lambda expression is used when we want function at once(single use function) .

# lambda action is  an anonymus function so it doesnot have a name to store the data.

# it is a single use function so it doesnot make sense to save the function data thats why it an anonymus(no name) function.

# syntax---> lambda param: action(param)
from functools import reduce
my_list = [1, 2, 3]
print(list(map(lambda item: item*2, my_list)))  # [2,4,6]
print(my_list)  # [1,2,3]
''' lambda is an one time run anonymus function so you donot
    need to run another time, or if interpreter run this function
    it doesnot remember the things but , it performs action in this single time of use '''
# if we want to use filter instead of map in lambda function
print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1,3]

# if we use reduce in lambda .........
print(reduce(lambda acc, item: acc+item, my_list))  # 6


################++++++++++++++++++#############=============#####################
##########################  LAMBDA EXPRESSION EXERCISE ##########################

# Square of our list given
mylist = [5, 4, 3]

new_list = list(map(lambda num: num**2, mylist))
print(new_list)  # [25, 16, 9]

# list sorting
# sorting accoring to 2nd value in each list i.e assending
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)  # [(10, -1), (0, 2), (4, 3), (9, 9)]
