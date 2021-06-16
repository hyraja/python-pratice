# findout reverse of given string

# method 1(Using loop)
# def reverse(s):
#     str = ''
#     for i in s:
#         str = i + str
#     return str


# print(reverse('rajaprasad')) # dasarpajar

# method 2(using indexing)
# def reverse(s):
#     p = s[::-1]
#     return p


# print(reverse('rajaprasad')) # dasarpajar

# method 3 (using reversed)
# def reverse(string):
#     string = ''.join(reversed(string))
#     return string

#   # dasarpajar
# s = 'rajaprasad'
# print(reverse(s))

# method 4(using reverse method)
s = [1, 2, 34, 67, 10, 9]
s.reverse()
print(s)  # [9, 10, 67, 34, 2, 1]
