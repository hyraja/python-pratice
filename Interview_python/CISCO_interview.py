# d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# d2 = {6: 'f', 7: 'g'}
# d1.update(d2)
# print(d1)

# Write a class with a constructor and a function "sum" which returns the sum of the parameters.. then create an object of the class and call the function "sum" and print output
# class SUMS:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def sums(self):
#         return self.num1 + self.num2


# c = SUMS(1, 2)
# print(c.sums())

# In a list, how to find non-repeating elements —> If a list has 10 items, and all of them are repeated twice except one
# a = [1, 1, 2, 3, 2, 3, 4, 5, 6, 4, 6, 5, 7, 8, 8, 9, 9]

# nr = [x for x in a if a.count(x) == 1]
# print(nr)

# a = {1: 'r', 2: 's', 3: 't', 4: 'u', 5: 'v', 6: 'w', 7: 'y'}
# b = ['r', 's', 'p', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #  Use list comprehension to find out the elements in b which are not present as values in a
# l_c = [x for x in b if x not in a.values()]
# print(l_c)
# # print(a.values())

# Reverse the string 'sdffs@zoc$nuklm' but do not reverse the special char answershould # 'mlkun@cox$sffds'
def reverse_string_without_affecting_number(text):
    temp = []
    text = list(text)
    for i in text:
        if not i.isnumeric():
            temp.append(i)
    reverse_temp = temp[::-1]
    count = 0
    for i in range(0, len(text)):
        if not text[i].isnumeric():
            text[i] = reverse_temp[count]
            count += 1
        else:
            continue
    return "".join(text)


print(reverse_string_without_affecting_number('sdffs@zoc$nuklm'))
