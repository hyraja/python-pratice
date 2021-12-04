# if __name__ == '__main__'
# this also a maintainer of this file


from modules_packages.shopping.shopping_cart import buy
from modules_packages.utility import multiply, divide


# modules_packages.shopping.shopping_cart ,this is for __name__
print(buy('orange'))
print(multiply(7, 6), divide(60, 10))  # modules_packages.utility
print(__name__)  # __main__

if __name__ == '__main__':
    print("ok i can run this")  # ok i can run this
''' if __name__ == '__main__': this statement states that if 
    __name__ is equal to __main__ then run the whole programme
    this the only way in python to run main file programme. '''

