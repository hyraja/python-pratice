

# we can call a function this way also.


def hello():
    print("helllllooooo")


greet = hello  # greet is pointing to hello function object
del hello  # after delete of hello greet still get answer

print(greet())  # helllllooooooo

# python function act like first class citizen

####################
# we can call a function as an argument


def helloo(func):
    func()


def greeet():
    print("still here")


a = helloo(greeet)  # greeet fun act like arguments of helllloooo function
print(a)  # still here
# python function act like argument


# ++++++++++++++++++++++++++++++++++++++++++++++
''' HIGHER ORDER FUNCTION (HOF) '''
# the function which accepts the function as a parameter or return function is called hof.
# ex: map,filter,reduce


def greet1(func):  # take function as parameter
    func()


def greet2():
    def func():
        return 5
    return func  # return function


print(greet1(greet2))

# ++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++


# DECORATORS


# --------------------------------------------------------------
''' using this features of function 'decorators' are made '''

''' decorators are supercharge the function, simply a function wrap another function
    and enhance it '''


# write our own decorator

def my_decorator(func):

    def wrap_func():
        print("********************")
        func()
        print("********************")

    return wrap_func


@my_decorator
def show():
    print("hello")


@my_decorator
def bye():
    print("see you later")


bye()
''' 
********************
see you later
********************
'''

show()
''' 
********************
hello
******************** 
'''
''' we are changing our function without change in show function
    we are just add one line like @my_decorator and change our function
    that is the power of decorator. '''

# undernith the decorator python interpreter call like this as a first class citizen.
show2 = my_decorator(show)
show2()    # we can write this in below way also

my_decorator(show)()
''' 
********************
hello
******************** 
'''
