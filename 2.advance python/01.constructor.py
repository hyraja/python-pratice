# constructors are call every time we instanciate an object.
# it is noted as __init__  .
# constructor will be automatically executed at the time of object creation.
# The main propose of constructor is to declare and initialize instance variable.
# per object constructor would be executed only once.
# constructor can take atleast one argument (atleast 'self')
# constructor is optional and if we are not providing any constructor python will pprovide default constructor.


class Playercharacter:
    def __init__(self, name, age):
        if (age > 18):  # we can get control over content according to our need.
            self.name = name
            self.age = age


player = Playercharacter('ronin', 90)
# object not created bcz age limit not reached
player1 = Playercharacter('tom', 10)

print(player.name)
print(player1.name)
