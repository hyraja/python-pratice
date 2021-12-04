# modules in python.

# every .py file  treated as module in python.

# we gonna import utility module to use it.


###########################
# packages
# package is a simple folder which contains multiple python module.

# we can call modules from different package like 'shopping'

import shopping.shopping_cart
import utility
# we can call directly  the function from modules.
# from utility import multiply,divide
# print(multiply(5,6))
print(utility)

''' <module 'utility' from 'd:\\gomoons\\python_pratice\\7.modules python\\01.modulehon_pratice\\7.modules python\\01s\\utility.py'> '''
# we can  call the function available in utility by using '. dot operator'.

print(utility.divide(10, 5))  # 2.0
print(utility.multiply(10, 10))  # 100

'''  This things available in utility.py file

def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


'''
print(shopping.shopping_cart.buy('apple'))  # ['apple']

# we call diiferent function from shopping package and inside module in this way
# from shopping.shopping_cart import buy
# print(buy('orange'))

''' we are also import multiply function/module from a packages by '* star symbol' '''
# from utility import *
