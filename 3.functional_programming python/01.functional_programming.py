# Functional Programming

# Goal for using Functional prohramming.
'''
    1. clear + Understandable
    2. Easy to Extend.
    3. Easy to Maintain.
    4. Memory Efficient.
    5. Dry
'''

# Functional Programming means use pure functions for all the things.

# we set our function to do proper work without side effect.

# if we run multiple time with same input our function gives us same result each  time.

# it provide a bug free programming

# Function doesn't interact with outside world.

# example:


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3, 4, 5]))  # [2,4,6,8,10]
