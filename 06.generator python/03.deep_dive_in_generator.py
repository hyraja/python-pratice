# Under the Hood of Generator.


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break


# special_for([1, 2, 3])
# # this is how for loop works undernith
# '''
# <list_iterator object at 0x000002133B91F048>
# 1
# <list_iterator object at 0x000002133B91F048>
# 2
# <list_iterator object at 0x000002133B91F048>
# 3
# <list_iterator object at 0x000002133B91F048> '''


# # how undernith how  next and iter and range are working .
# class Mygen():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if Mygen.current < self.last:
#             num = Mygen.current
#             Mygen.current += 1
#             return num
#         raise StopIteration


# gen = Mygen(0, 10)
# for i in gen:
#     print(i)
# '''
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 '''

# Generating an infinite sequence, however, will require the use of a generator, since your computer memory is finite:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# This code block is short and sweet. First, you initialize the variable num and start an infinite loop.
#  Then, you immediately yield num so that you can capture the initial state. This mimics the action of range().
# After yield, you increment num by 1. If you try this with a for loop, then you’ll see that it really does seem infinite:
for i in infinite_sequence():
    print(i, end=" ")
