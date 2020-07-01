# Private and public variable
# it is the rule in python single underscore is treated as private like:
# _name but in python true private is not present for developer.


class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and my age is {self._age}')


player1 = PlayerCharacter('raja', 23)
# player1.speak()

'''when i write below code it override all the things
 and it is a problem in abstraction so in python public
  and private variable concept is present'''


# we can over ride private  with this attribute so i can say there is no private for developer.
player1.name = '!!!!'
player1.speak = 'BOOO'

# print(player1.speak())
print(player1.speak)


# double underscore in python is called dunder method.
# you are not have to write your own dunder method in python because there is
# a chance to override the default thing which are present in python.
