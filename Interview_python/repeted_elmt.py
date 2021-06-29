# Count Repeated element in the list [duplicate]

# method 1 (native)
# mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 43]
# count = 0
# for i in mylist:
#     if i == 1:
#         count += 1

# print('number of 1 present in list ', count)
# number of 1 present in list 2

# method 2 (using count)
# mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 43]
# mylist1 = mylist.count(1)
# print(type(mylist1)) # int
# print('number of 1 present in list', mylist1)
# number of 1 present in list 2

# method 3(stote the repeate time element in dictionary)
# mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 43]
# duplicate_dict = {}
# for i in mylist:
#     duplicate_dict[i] = str(mylist.count(i)) + ' times repeated'
# print(duplicate_dict)
''' 
{1: '2 times repeated', 2: '2 times repeated', 3: '2 times repeated', 4: '2 times repeated', 5: '2 times repeated', 
43: '1 times repeated'}
'''

# method 4(using dictionary comprehension)
# mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 43]
# duplicate_dict = {i: str(mylist.count(i))+' times repeated' for i in mylist}
# print(duplicate_dict)
''' 
{1: '2 times repeated', 2: '2 times repeated', 3: '2 times repeated', 4: '2 times repeated', 5: '2 times repeated', 
43: '1 times repeated'}
'''

# method 5 (using counter)

# we need to import counter function
# from collections import Counter
# mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 43]
# duplicate_dict = Counter(mylist)
# print(duplicate_dict)  # Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 43: 1})
# print(duplicate_dict[1]) # 2


# s = 'suresssh'
# print(s.count('s'))#4


# mylist = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
# newlist = []
# [newlist.append(i) for i in mylist if mylist.count(i) > 1 if i not in newlist]
# print(newlist) # [1, 2, 3, 4]
