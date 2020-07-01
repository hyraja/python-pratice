# Attributes and Methods

# Attributes: attributes in the sense the properties of the class.

# Methods: methods are called action of the class and it is the simple function which are declared inside a class.


class PlayerCharacter:
    # class object attribute : class object doesnot change in all objects.
    membership = True

    def __init__(self, name, age):
        if(self.membership):
            self.name = name  # attributes
            self.age = age  # attributes

    def shout(self):  # methods
        print(f'my name is {self.name}')
        print('done')

    def run(self, hello):  # methods
        print(f'my age is {self.age}')
        print('run')


player1 = PlayerCharacter('rony', 33)
player2 = PlayerCharacter('tom', 22)

# help(player1)  # list of weak references to the object (if defined)

print(player1.name, player1.age)  # rony 33
print(player2.name, player2.age)  # tom 22
print(player1.membership)  # True
print(player2.membership)  # True
print(player1.shout())
print(player2.shout())
print(player1.run('hello'))
