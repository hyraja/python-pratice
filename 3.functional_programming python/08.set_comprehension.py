# set and dictionary comprehension

# set comprehension is a quick way to generate set, set doesnot allow duplicates

myset = {char for char in 'hello'}
print(myset)  # {'o', 'h', 'l', 'e'}

numset = {num for num in range(0, 10)}
print(numset)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

square_set = {num**2 for num in range(0, 10)}
print(square_set)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

evensquareset = {num**2 for num in range(0, 10) if num % 2 == 0}
print(evensquareset)  # {0, 64, 4, 36, 16}


#################################################################
##### dictionary comprehension #############################

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)  # {'b': 4}


# question: item is the key and item multiply by 2 is the value of dict using given list [1,2,3].

mydict = {num: num*2 for num in[1, 2, 3]}
print(mydict)  # {1: 2, 2: 4, 3: 6}


############################################################################
########### exercise comprehension #######################
# Q: findout duplicate from given list and save the duplicate into an another list using list comprehension.

some_list = ['a', 'b', 'c', 'b', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)  # ['b', 'n']
