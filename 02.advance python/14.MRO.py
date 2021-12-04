# MRO - Method Resolution Order
# mro decide which function/attribute execute when


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


'''
           A
         /    \
        /      \
       B        C
        \       /  this is the figure i explain above
         \     /
            D
'''
print(D.num)  # 1

''' both num variable is
present in A as well as in c but it gives 1 as
mentioned in C class. bcz of mro.
 to find out mro of class use mro() function like below '''

print(D.__mro__)  # 1 both are same
print(D.mro())
'''[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]'''
''' it given D --> B --> C --> A --> object(object is the base class where all the class inherite from in python) '''
# D.__str__ if we are not providing any value inside class and want to check __str__ present in object, then it give whole mro
