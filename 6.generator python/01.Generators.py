# Generators in python.


''' 
Generator functions allow you to declare a function that behaves like an iterator. 
They allow programmers to make an iterator in a fast, easy, and clean way. ...
 An iterator is an object that can be iterated (looped) upon '''

''' generators allow us to generate sequence of value over time. '''

# ex:
''' range is a generator it genertaes  items. '''
list(range(100))


# ex:
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


mylist = make_list(100)
print(mylist)


# Iterable
''' iterable in python is any object which can loop through
   undernith it is using __iter__ method '''

# Iterate / Iteration
''' the act of taking iterables and doing the work like for loop,while loop '''

# Generators
''' all generators are iterable but all itearbles are not generators '''
''' generators are different from iterables i.e all iterable are store in memory
    but generator store single element and keep going by next and next...accordingly. '''
''' generator only remember the most recent data '''

# define generators


def generator_function(num):
    for i in range(num):
        yield i  # yield pauses the function


for item in generator_function(10):
    print(item)
'''
0
1
2
3
4
5
6
7
8
9
'''


# yield and next ..

def generator_func(num):
    for i in range(num):
        yield i*2


g = generator_func(100)
print(next(g))  # 0  1st 0*2 = 0
print(next(g))  # 2  2nd 1*2 = 2
print(next(g))  # 4  3rd 2*2 = 4
print(next(g))  # 6  4th 3*2 = 6

''' yield pause the function and only remember the most recent one value 
    and next() gives the next iterables '''

'''
In summary…
Generators allow you to create iterators in a very pythonic manner.
Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets.
Iterators and generators can only be iterated over once.
Generator Functions are better than Iterators.
Generator Expressions are better than Iterators (for simple cases only). '''
