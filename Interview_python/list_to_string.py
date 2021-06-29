# we want to convert list into string

# method 1
# s = ['Geeks', 'for', 'Geeks']
# s1 = ' '
# for item in s:
#     s1 += item
# print(s1) #  GeeksforGeeks

# Method #2: Using .join() method

# Python program to convert a list
# to string using join() function

# Function to convert
# def listToString(s):

#     # initialize an empty string
#     str1 = " "

#     # return string
#     return (str1.join(s))


# # Driver code
# s = ['Geeks', 'for', 'Geeks']
# print(listToString(s)) #Geeks for Geeks

# method 3 using list comprehension
# s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# # using list comprehension
# listToStr = ' '.join([str(elem) for elem in s])

# print(listToStr) # I want 4 apples and 18 bananas

# method 4: using map method

# s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# # using list comprehension
# listToStr = ' '.join(map(str, s))

# print(listToStr)


# _____________________________________
# i want to write the string with reverse format
#  'good to look' --- > 'look too good'

s = 'good too look'
spliter = s.split()
spliter.reverse()
print(' '.join(spliter))  # look too good
