# sometimes we have attributes are associates with the  class
#  not with each instance of class.

# or in other way, we would like to have attributes whose value
# will be shared with all instances of the class such attributes
# are called class attributes.
#
# EX: Class Attributes Syntax
'''
class Myclass:
    # Define class attributes inside class block
    myclass_attribute = "class attributes goes here"
    my_constants = "They are often class-specific constants"

    def __init__(self):
        self.my_instance_attribute = "instance attributes are here"
'''

# scopes in python
'''
LOCAL     -> inside current function
Enclosing -> inside enclosing function
GLOBAL    -> At the top level of the module
Built-in  -> In the special built-in functions
'''

# real example:


class ShippingContainer:
    next_seriel = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.next_seriel = ShippingContainer.next_seriel
        ShippingContainer.next_seriel += 1


C4 = ShippingContainer('ESC', ['Electronics'])
print(C4.next_seriel)  # 1337

C5 = ShippingContainer('ESC', ['pharmacuticals'])
print(C5.next_seriel)  # 1338

# we can get the class attribute value by class name or the object name
# which we created
print(ShippingContainer.next_seriel)  # 1339

# N.B there is no class scope in python

# recap


class myclass:

    b = "On class"

    def __init__(self):
        self.a = "on instance"
        print(self.a)
        print(myclass.b)
        print(self.b)    # access the class attributes
        self.a = "rebound"  # re-bind the existing instance attributes
        self.b = " new on instance"  # instance attributes hide the class attributes
        print(self.b)  # access the instance attribute throgh self
        print(myclass.a)  # access class attribute via class object.
