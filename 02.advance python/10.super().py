
# SUPER()


class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)  # one way
        super().__init__(email)  # another way
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


wizard1 = Wizard('merlin', 60, 'merlin@gmail.com')
# print(wizard1.sign_in())  # it gives 'logged in' as a result.
# it doesnot give answer bcz wizard1 object have no access to email attribute,
# print(wizard1.email)
# this is bcz user and wizard both have constructor so there is two way
# to solve this problem i.e define email in wizard parameter and another
# one is to User.__init__(self, email) provide this field inside wizard and also provide email attribute in wizard class.

# after that we can see the answer

print(wizard1.email)  # merlin@gmail.com


# and also there is anather way to do this using super() keyword
# super() is refering to super class.
# using super we are no longer to use self keyword.
