# a = [1, 2, 3, 4]
# b = a
# b[1] = "raja"
# print(b)  # [1,'raja',3,4]
# print(id(b))  # 2835871524416
# print(a)  # [1,'raja',3,4]
# print(id(a))  # 2835871524416

''' 
In Python, we use = operator to create a copy of an object.
it will not only create a new variable(b), also create new
variable that shares the reference of original object.

as we can able to see the o/p as both share the same id.

if we want to change any values in a or b , the changes will visible in both.

'''

# in python we use copy module for shallow and deep copy operations.
# import copy
# copy.copy(x) ## it will give o/p as shallow copy of x
# copy.deepcopy(x) ## it will give o/p as deep copy of x.
