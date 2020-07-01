# -----------------Topics---------------------------
# 1. what is dictionary
# 2. adding and removing values
# 3. Iterating through dictionary.
# 4. Tuples
# ---------------------------------------------------

# Dictionary allows to store vakue through key and value pair.
# in dictionary order doesn't matter.
# ex: telephone books

d = {'tom': 9090900126, 'bob': 9090900127, 'kenny': 9090900128}
print(d)  # {'tom': 9090900126, 'bob': 9090900127, 'kenny': 9090900128}
print(d['tom'])  # 9090900126
d['sam'] = 9090900129
# {'tom': 9090900126, 'bob': 9090900127, 'kenny': 9090900128, 'sam': 9090900129}
print(d)
del(d['sam'])  # it will delete the specified item
print(d)  # {'tom': 9090900126, 'bob': 9090900127, 'kenny': 9090900128}

# iterate through the dictionary.
for key in d:
    print(f'key: {key} value : {d[key]}')
    ''' key: tom value : 9090900126
        key: bob value : 9090900127
        key: kenny value : 9090900128 '''

# iterating through for loop.
for k, v in d.items():
    print(f'key: {k} value : {v}')
    ''' key: tom value : 9090900126
        key: bob value : 9090900127
        key: kenny value : 9090900128 '''

# wipe out all data from dictionary:
d.clear()
print(d)  # {}


########################################## Tuples #########################
# tuples is a list of value grouped together.
#  tuples all values are different menaing(heterogeneous)
# ex: point=(4,5)  4 is x coordinate and 5 is y coordiante.
# ex2: adress=("murgeshpallaya","bengaluru",560017)
# tuples are immutable.
point = (5, 9)
print(point)  # (5,9)
print(point[0])  # 5

point[0] = 50
print(point)  # TypeError: 'tuple' object does not support item assignment
