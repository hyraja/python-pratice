######################Json###########################
# 1. what is Json.
# 2. Json vs XML.
# 3. create address book using JSON format.
#####################################################
# JSON---> javascript object Notation
# Json is a data exchange format similar to xml.
# json is light weight as compare to xml.

# ---------------------------------------------------------------
# we write an address book in json format.
# ---------------------------------------------------------------
import json
book = {}
book['tom'] = {
    'name': 'tom',
    'address': 'murgeshpallaya',
    'phone': 909090
}
book['bob'] = {
    'name': 'bob',
    'address': 'murgeshpallaya',
    'phone': 6060660
}
# get the input as book element and dump into in string so 'dumps' used. and then convert into json format.
s = json.dumps(book)
# print(s)
with open("D:\\Workspace\\pratice@Python\\json-data.txt", "w") as f:
    f.write(s)

########### read the data from  json ########################
f = open("D:\\Workspace\\pratice@Python\\json-data.txt", "r")
s1 = f.read()
print(s1)
print(type(s1))  # <class 'str'>
book1 = json.loads(s1)  # loads convert the json string into dictionary object
print(book1)
print(type(book1))  # <class 'dict'>
print(book['bob'])
#{'name': 'bob', 'address': 'murgeshpallaya', 'phone': 6060660}
print(book['bob']['phone'])  # 6060660

######################## using for loop########################
for person in book1:
    print(book1[person])
'''
{'name': 'tom', 'address': 'murgeshpallaya', 'phone': 909090}
{'name': 'bob', 'address': 'murgeshpallaya', 'phone': 6060660} '''
