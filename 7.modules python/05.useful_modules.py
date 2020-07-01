
from array import array
import datetime
# from collections import defaultdict, Counter, OrderedDict

# sentence = 'i am going to office everyday.'
# li = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10]
# # Counter({8: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 10: 1})
# print(Counter(li))
# # counter counts how many times iterable items are present .
# print(Counter(sentence))
''' Counter({' ': 5, 'i': 3, 'o': 3, 'e': 3, 'a': 2, 'g': 2, 'f': 2, 'y': 2, 
'm': 1, 'n': 1, 't': 1, 'c': 1, 'v': 1, 'r': 1, 'd': 1, '.': 1}) '''


####################################
# datetime module

# import datetime
print(datetime.time())  # 00:00:00
print(datetime.time(5, 45, 6))  # 05:45:06
print(datetime.date.today())  # 2020-03-27
print(datetime.datetime.now())  # 2020-03-27 01:24:18.884378

##############################################
# array module
#from array import array

arr = array('i', [1, 2, 3, 4, 5, 6])
print(arr)  # array('i', [1, 2, 3, 4, 5, 6])
''' it is more faster than list,so it is uses for optimization '''
