
# The split() method splits a string into a list.

# You can specify the separator, default separator is any whitespace.

# string.split(separator, maxsplit)

# txt = "welcometothejungle"
# x = txt.split()
# print(x)
# print(type(x))
# ['welcometothejungle']
# <class 'list'>

# --------------------------

# txt = "welcome to the jungle"
# x = txt.split()
# print(x)
# print(type(x))
# ['welcome', 'to', 'the', 'jungle']
# <class 'list'>

# setting the maxsplit parameter to 1, it will omit $ from the first ouccurance
# h = 'Hello$world$'
# x = h.split('$', 1)
# print(x)
# ['Hello', 'world$']

#  first i omit '$' and add 2 element of list with '_'
h = 'Hello$world$'
x = h.split('$')
y = x[0] + '_' + x[1]
print(y)
# Hello_world

#  small a is not equal to capital A
print(ord('a'))  # 97
print(ord('A'))  # 65

print(chr(97))  # a
print(chr(65))  # A
