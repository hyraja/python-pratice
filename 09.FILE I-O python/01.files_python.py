# FILE I/O


my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())  # to read file
# hy my name is rajaprasad
''' if we multiple time use read command it 
    gives the most recent one as an answer. '''

''' seek remind the cursor position  to start counting then 
    if you can run read command multiple time it gives answer '''

# print(my_file.readline())  # it only read the first line of the class.

print(my_file.readlines())
# it gives all the line available in file with  list format
''' ['hy my name is rajaprasad\n', ':)\n', 'how are you?'] '''

# with done all your work need to close file manually.
my_file.close()
