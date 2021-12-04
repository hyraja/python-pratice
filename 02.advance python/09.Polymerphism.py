# POLYMERPHISM

# poly means 'many'
# merphism means 'forms'


class User(object):
    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")


class Wizard(User):  # this class inherited from User class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # i can also pass main class method also with same name
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f' Archer attacking with arrows of : {self.num_arrows}')


wizard1 = Wizard('merlin', 50)
archer1 = Archer('robin', 500)


wizard1.attack()  # attacking with power of 50
archer1.attack()
# polymerphism: this means many forms but single method name .
# ex: attack method is used for  archer and also for wizard but different attributes for each.


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

# i can wrap attack method with using function as given

# I can also doing in this way: using for loop
for char in [wizard1, archer1]:
    char.attack()


# polymerphism allow us to have many form it is the ability to redifine the methods for this derived classes i.e wizard and archers.
