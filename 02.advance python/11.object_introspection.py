# OBJECT INTROSPECTION
'''OBJECT INTROSPECTION is the ability
 to determine/inspect the type of object in runtime'''


class User(object):
    def __init__(self, email):
        self.email = email
        print("init complete")

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('hellin', 60, 'hellin@gmail.com')
print(dir(wizard1))

'''
ans : init complete
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']


'''

# using dir()method we are able to see our instance is containing which  attribute or methods so this is called object introspection.
