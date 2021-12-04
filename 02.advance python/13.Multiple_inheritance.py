# Multiple Inheritance


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print("ran really fast")


# it inherited from multiple class so called multiple inheritance.
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):  # this is the solution for below problem
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('raja', 50, 100)
print(hb1.run())  # ran really fast so it's work fine.
print(hb1.check_arrows())  # 100 remaining
# AttributeError: 'HybridBorg' object has no attribute 'arrows'
'''technically we instatiate the object with 1st 'Wizard' then 'Archer'
thats why we are not able to provide 3 arguments 
to overcome this situation we provide constructer inside HybridBorg'''

print(hb1.attack())
''' it doesnot work  properly so you need to provide 
Wizard.__init__(self,name,power) inside HybridBorg class.'''

print(hb1.sign_in())  # logged in  ,, it works
