# ABSTRACTION

# abstraction means hiding of data or abstract the way information and giving access to what only necessery.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and my age is {self.age}')


player1 = PlayerCharacter('raja', 23)
player1.speak()

# we can see here the abstraction like
# when i call the player1.speak() but i don't need to know how speak is implemented.

# we also seen these example with all our data type like
# list:
# 2  i get the answer that 2 is written 2 times in that list
print([1, 2, 3, 4, 1, 2].count(2))
# because of count method but i don't know how count method  is implemented in python so that is abstraction.
# ex2:
#  it gives 5 is the length but i really don't care about how length method is implemented.
print(len((1, 2, 3, 4, 5)))  # 5

# ex3:
# camera in iphone is to take photo but we don't know how camera function coded it is also a abstraction.


#######################################################################################################
# Abstract method
###################################################################
''' sometimes we donot know about implemenation, still we can
    declare a method. Such types of methods are called Abstract method
    'this method has only declaration not implementation' '''
# in python we can declare abstract method using @abstractmethod decorator.
# @abstractmethod present inside abc module, first call that one.

# ex:

# from abc import abstractmethod
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass
# child class is responsile to provide implementation for parent class abstarct method.


#####################################
# Abstract Class
#####################################
''' sometimes implementation of class is not complete,
    such type of partially implementation classes are called
    abstract class.Every abstract class in python should be
    derived from ABC class which is present in abc module '''
# ex1

# from abc import *


# class Test(ABC):
#     pass


# t = Test()
# _____________________________________________________


# ex2:

# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         print('hello')


# t = test()
# t.m1()  # hello


# note:
''' if a class contains atleast on abstract method and if we extending
 ABC class then instatiation is not possible. '''
# abstract class with abstract method instantiation is not possible.
# parent class abstract method should be implemented in child class.

#############################
# Interface
#############################
''' if the abstract class contains only abstract methods such type
of class considered as interface '''
# ex:

# from abc import *


# class DBInterface(ABC):
#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def disconnect(self):
#         pass
# # we are only provide the abstract method and these are used by
# # child classes right below.
# # child class call these methods and give their value.


# class Oracle(DBInterface):
#     def connect(self):
#         print('connecting to oracle database')

#     def disconnect(self):
#         print('disconnecting from oracle database')


# db = Oracle()
# print(db.connect)
# print(db.disconnect)
#############################################################
# Abstract class VS Interface VS Concrete class
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Interface :
''' if we donot know anything about implementation just we have 
    requirement specification then we should go for interface. '''
# Abstract class:
''' if we are talking about implementation but not completely 
 then we should go for abstract class(partially implemented class) '''
# Concrete class:
''' if we are talking about implementation completely and ready to 
 provide service then we should go for  concrete class '''

# ex:
# from abc import *


# class Automation(ABC):
#     # interface
#     @abstractmethod
#     def manpower(self):
#         pass

#     @abstractmethod
#     def idea(self):
#         pass

#     @abstractmethod
#     def money(self):
#         pass


# class AbsCLs(Automation):
#     # Abstract class
#     def manpower(self):
#         print('man power are collected for automation project')

#     def idea(self):
#         print('students are enough idea to success the project')


# class ConcreeCLs(AbsCLs):
#     def money(self):
#         print('college provided th fund for this project')


# automationproject = ConcreeCLs()
# automationproject.manpower()
# automationproject.idea()
# automationproject.money()
