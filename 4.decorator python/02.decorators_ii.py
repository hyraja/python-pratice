# decorators pattern

# decorator pattern gives us flexibility to give multiple arguments
# to the wrap_function as *args,**kwarrgs  and unpack with using func(*args,**kwargs)
# so we can give multiple parameter to our hello() function.


from time import time


def my_decorator(func):
    def wrap_func(greeting):
        print("$"*20)
        func(greeting)
        print("$"*20)

    return wrap_func


@my_decorator
def hello(greeting):  # if we want to pas an arguments
    print(greeting)


hello("hiii")
'''
$$$$$$$$$$$$$$$$
hiii
$$$$$$$$$$$$$$$$
'''  # we pass an argumet in our hello() function, underneth python interpreter
# call this way 'a = my_decorator(hello); a("hii")'
''' when we add multiple parameter to our function ,we need to provide
    multiple parameter in wrapper function so it is very haptic thats why we add
    *args and **kwargs inside wrapper function and also inside func()
'''


def my_decorator2(func):
    def wrap_func(*args, **kwargs):

        func(*args, **kwargs)

    return wrap_func


@my_decorator2
def hello2(greeting, emoji=':('):  # if we want to pass multiple arguments
    print(greeting, emoji)


hello2("hiii")  # hiii :(


# ====================================================================================
# why do we need decorator ?

''' i want to check how our code execute in what time it takes  using decorator '''


def performance(fn):
    def wrapper(*args, **kwargs):
        initial_time = time()
        result = fn(*args, **kwargs)
        finish_time = time()
        print(f'took {finish_time-initial_time}s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()  # took 0.010499954223632812 s
''' using the @performance decorator i can meausure the time, function need to fnish
    and also measure in any function.
'''
