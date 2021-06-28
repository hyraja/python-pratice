''' 
The join() method is a string method and returns a string 
in which the elements of sequence have been joined by str separator.

Syntax:

string_name.join(iterable) 

string_name: It is the name of string in which joined elements of iterable will be stored.
Parameters: The join() method takes iterable – objects capable of returning its members one at a time. 
Some examples are List, Tuple, String, Dictionary and Set

Return Value: The join() method returns a string concatenated with the elements of iterable.

Type Error: If the iterable contains any non-string values, it raises a TypeError exception.
'''

# list1 = ['1', '2', '3', '4']

# s = "-"

# # joins elements of list1 by '-'
# # and stores in sting s
# s = s.join(list1)

# # join use to join a list of
# # strings to a separator s
# print(s) # 1-2-3-4

# joining with empty string
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))  # geeks
print(' '.join(list1))  # g e e k s
print(' - '.join(list1))  # g - e - e - k - s
