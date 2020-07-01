# INHERITANCE

'''
Inheritance allows new objects to take on the properties of
existing objects.
---> you can inherit classes as well in  below given .
'''


class User(object):

    def sign_in(self):
        print('logged in')


class Wizard(User):  # this class inherited from User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):  # this class inherited from User class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f' Archer attacking with arrows of : {self.num_arrows}')


wizard1 = Wizard('merlin', 50)
archer1 = Archer('robin', 500)
# print(wizard1.sign_in())  # logged in
wizard1.attack()  # attacking with power of 50
archer1.attack()  # attacking with arrow of : 500

# Both wizard class and archer class are access of different methods
# and also both having access of sigh_in method so that is the power of inheritance
archer1.sign_in()  # both accessing siign_in method
wizard1.sign_in()


# python gives us a function to check the instance and class
print(isinstance(wizard1, Wizard))  # True
# True bcz wizard1 is inherited from object class that is parent class.
print(isinstance(wizard1, object))  # True
