# ZIP()

# zip means to pack of two or more list into a single zip box.

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 80, 98)


print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]

print(list(zip(my_list, your_list, their_list)))
''' [(1, 10, 5), (2, 20, 80), (3, 30, 98)] '''
print(my_list)  # [1,2,3]

# zip is like a zipper and take multiple iterable and zip their items accordingly.
# it can zipping different iterable like list and tuple.

''' ex: If in our database user name is in a column and phone number 
in another column , if you want to bind these in a single place
 then that time we need to zip these two iterables .so that it 
 can be shown as ['username', phone_number] '''

''' zip iterate whole the data structures and zipping items together '''
# we don't modify the current data structure it creates a whole new data structure  and zipping elements accordingly.


# Unzipping the file:
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
print(list(zip(*test_list)))
#[('Akshat', 'Bro', 'is', 'Placed'), (1, 2, 3, 4)]

# using list comprehension to perform Unzipping
res = [[i for i, j in test_list],
       [j for i, j in test_list]]
print(res)
#[['Akshat', 'Bro', 'is', 'Placed'], [1, 2, 3, 4]]

# Unzip a list of tuples  using map()
res2 = map(None, *test_list)
print(str(res2))
# <map object at 0x000001EF78D7FA58>
