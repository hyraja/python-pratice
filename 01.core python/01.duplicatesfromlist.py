#find duplicates from given list.

some_list = ['a','b','b','c','d','d']

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)