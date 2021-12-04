# class method: because it doesnot need to instantiate for object creation,
# you can call your method by class name and 'cls' is use rather than self.
#  this class method is called by class name so it is called @classmethod
# we are using class method to change the default constructor parameters on runtime


# staticmethod: it is exactly same as classmethod but it doesnot use 'cls'
# staticmethod doesnot care about the class properties/attributes.


# Both classmethod and static method are called without instantiate .


class PlayerCharacter:

    membership = True

    def __init__(self, name, age):
        if(self.membership):
            self.name = name  #
            self.age = age  #

    def shout(self):  # methods
        print(f'my name is {self.name}')

    @classmethod  # it is a class method
    # cls ---->class, is the standard as like of self  we can use anything.
    def adding_things(cls, num1, num2):
        # return num1 + num2
        return cls('teddy', num1 + num2)

    @staticmethod
    # staic method is same like classmethod but it doesnot use cls keyword
    # this staticmethod doesnot care about class state like properties/attributes of class.
    def adding(num1, num2):
        return num1 + num2


# print(PlayerCharacter.adding_things(3, 5))  # 8 # it is called by class name so it is called classmethod
# print(player1.adding_things(2, 3))  # 5
# we can also create a new object using class method.
player3 = PlayerCharacter.adding_things(2, 5)
print(player3.name)  # teddy
print(player3.age)  # 7

player4 = PlayerCharacter.adding(3, 7)
print(player4)  # 10


# Difference between staticmethod and classmethod

# Official python docs:

# @classmethod

# A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

# class C:
#     @classmethod
#     def f(cls, arg1, arg2, ...): ...
# The @classmethod form is a function decorator – see the description of function definitions in Function definitions for details.

# It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.
#  If a class method is called for a derived class, the derived class object is passed as the implied first argument.


# @staticmethod

# A static method does not receive an implicit first argument. To declare a static method, use this idiom:

# class C:
#     @staticmethod
#     def f(arg1, arg2, ...): ...
# The @staticmethod form is a function decorator – see the description of function definitions in Function definitions for details.

# It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.
