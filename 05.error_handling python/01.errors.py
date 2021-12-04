# Errors in python

''' errors that crashes our programme is called exception in python. '''
# ex:
# print('hello)  # SyntaxError: EOL while scanning string literal
# print(1+'hello')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# python built-in exceptions
''' https://docs.python.org/3/library/exceptions.html '''

# syntax error:


# def hooo()  # i am not providing : so it gave syntax error
def hooo():

    # name error
    # 1+name  # NameError: name 'name' is not defined

    # index error
    ''' li = [1, 2, 3]
        li[5]  # IndexError: list index out of range '''

   # key error
   # di = {'a': 1}
   # di['b']  # KeyError: 'b'

# zero division error
    5/0  # ZeroDivisionError: division by zero


hooo()  # SyntaxError: invalid syntax
