# what is oops --> object oriented programmings.
# ans : oops is a paradigm to organise our code that should be managable and clean and small.
# example:

# AMAZON DRONE
# drone  have different parts assamble and each part like propeler,motor,cpu should be trated as a single object and
# when we create another drone we should use these objects


## CLASS ##
# ----> class is a blue print to create different object
class Big:  # class
    pass


object = Big()  # instantiate a class by new object
object2 = Big()  # instantiate
print(type(object))  # <class '__main__.Big'>


##################################################
# creating our own object
# for wizard game
class PlayerCharacter:
    # class object Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name  # Attribute/properties
        self.age = age  # Attribute/properties

    def run(self):  # method/instance method
        print('run')
        return 'done'  # a method should be return something oterwise it gives error


player1 = PlayerCharacter('rony', 22)
player2 = PlayerCharacter('tom', 67)

# help(player1) it gives whole details of an object
print(player1.name, player1.age)  # rony 22
print(player2.name, player2.age)  # tom 67
print(player1.run())  # run done
print(player1.membership)  # True
print(player2.membership)  # True
