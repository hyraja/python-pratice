# Under the Hood of Generator.


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])
# this is how for loop works undernith
'''
<list_iterator object at 0x000002133B91F048>
1
<list_iterator object at 0x000002133B91F048>
2
<list_iterator object at 0x000002133B91F048>
3
<list_iterator object at 0x000002133B91F048> '''


# how undernith how  next and iter and range are working .
class Mygen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Mygen.current < self.last:
            num = Mygen.current
            Mygen.current += 1
            return num
        raise StopIteration


gen = Mygen(0, 10)
for i in gen:
    print(i)
'''
0
1
2
3
4
5
6
7
8
9 '''
