# ENCAPSULATION

# The encapsulation means binding of data and the functions that manipulate the data.
# then we encapsulate  big object and store in small small box so user, machine can interact with them.

# data is the attributes we are given in class

# example


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    # we are encapsulating/packaging the class attributes into an method
    def speak(self):
        print(f'my name is {self.name} and my age is {self.age}')


player1 = PlayerCharacter('raja', 23)
player1.speak()

''' we can see the live example of encapsulation in this way

 when we write a string or any data type and give a dot '.' in my editor prompt different methods
 this is all happen by the help of encapsulation
 in python that  they are write different methods for 'string'
 or any data types and encapsuated with all the class.
so thats why when we write a dot after anydata type it prompts different method
'''

# encapsulation gives us true power
# so we  use different methods or action to use for our need.
