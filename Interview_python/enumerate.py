# The enumerate() method adds counter to an iterable and returns it (the enumerate object).

# The syntax of enumerate() is:

# enumerate(iterable, start=0)
# enumerate() Parameters
# enumerate() method takes two parameters:

# iterable - a sequence, an iterator, or objects that supports iteration
# start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.

# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))  # Return type: <class 'enumerate'>
print(list(enumerate(l1)))  # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))  # [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
