# DUNDER METHOD

'''using this dunder method , list is accessed by[]index 
   and dictionary access by 'key. and all data type also'''


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

        # lets customize own dunder method
    def __str__(self):
        return f'{self.color}'
        '''
        after modification you instaciate object and also
        when you call __str__ method it gives red .
        '''
        #'''we can change meaning of length in this way below'''

    def __len__(self):
        return 5

    # we can also change the del method and also all dunder method.
    def __del__(self):
        print("deleted!")

    def __call__(self):
        return ('yess>>')

    def __getitem__(self, i):  # using this we need to add an attribute my_dict in class
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())  # <__main__.Toy object at 0x000001FAD5BDF1D0>
print(str(action_figure))  # <__main__.Toy object at 0x000001FAD5BDF1D0>

# these two are giving same result

print(len(action_figure))  # 5


# del action_figure  #-----> deleted!


print(action_figure())  # yes>>

print(action_figure['name'])  # yoyo


#############################################
# extending list using dunder method:
############################################
class SuperList(list):  # if we are not providing 'list' here then
    # we are not able to use list function like 'append'
    def __len__(self):
        return 1000


Superlist1 = SuperList()

print(len(Superlist1))  # 1000
# this append function we are use bcz of list provided in parent class.
Superlist1.append(5)
print(Superlist1[0])  # 5
print(issubclass(SuperList, list))  # True
print(issubclass(list, object))  # True
