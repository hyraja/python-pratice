# python built_in modules
''' https://docs.python.org/3/py-modindex.html '''


# import random

# help(random) it giving all the info about random library
# print(dir(random))
''' ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'] '''


# print(random.random())  # 0.7760221433317678
''' its giving a random number between 0-1 '''

# print(random.randint(1, 100))
''' randint gives us random inter in the given interval. '''

# print(random.choice([1, 2, 3, 4, 5]))
''' it gives choices everytime we run from given list. '''


# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)  # [3, 5, 1, 4, 2]
''' it shuffle our list. '''

''' we can import our module  using alising to avoid name collisiom '''
# import random as r


''' at the place of random we use 'r'. In case we are alising and 
using random it gives error '''


############################################
# another built-in modules

# sys


# import sys
# first = sys.argv[1]
# last = sys.argv[2]

# print(f'hiii {first} {last}')  # hiii raja prasad
''' argv modules grasp the commandline argument you are give to 
    this file through command line like 'py 03.Built-in.py raja prasad'
    here first argument through cmd is 'raja' and 2nd is  'prasad' '''
import math
print(dir(math))
