# list ,set ,dictionary comprehnsion

# it is the quick way to generate iterable like list, set, dictionary
#  instead of looping or appending bunch of items.

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)  # ['h', 'e', 'l', 'l', 'o']
''' we created ['h', 'e', 'l', 'l', 'o'] list using this looping
but there is an easy way to create it, that is list comprehension '''

# list comprehnsion example
mylist = [char for char in 'hello']
print(mylist)  # ['h', 'e', 'l', 'l', 'o'] same result as above

# we want a number of 0 to 100 in list comprehnsion
numlist = [num for num in range(0, 100)]
print(numlist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 2 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 3, 41, 42, 43, 44, 45,49, 50, 51, 5, 54,, 55, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,2, 63, 64, 65, 66, 6774, 75, 76, 7 80, , 8 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 684, 85, 86, 87, 88, 899]8, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] '''

# we want to square of all the element in list:
squarelist = [num**2 for num in range(0, 10)]
print(squarelist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# we want to square of item and only show even  number of squarelist.
evensquare = [num**2 for num in range(0, 10) if num % 2 == 0]
print(evensquare)  # [0, 4, 16, 36, 64]
