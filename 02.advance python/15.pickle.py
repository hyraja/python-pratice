
# pickling and unpickling.

''' the process of writting state of objects to the file is called pickling or serialize the object with binary format '''
''' the process of reading state of objects from the file is called unpickling or deserialize the object from binary format to object. '''
# pickle module contains dump() to perform pickling.
# pickle module contains load() to perform unpickling.
# ex:

# import pickle


# class Employee:
#     def __init__(self, eno, ename, esal, eaddr):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.eaddr = eaddr

#     def display(self):
#         print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr)


# # pickling
# with open('emp.dat', 'wb') as my_file:
#     e = Employee(100, 'Raja', 100000, 'Bangalore')
#     pickle.dump(e, my_file)
#     print('pickling of employee object complete')

# # unpickling
# with open('emp.dat', 'rb') as f:
#     obj = pickle.load(f)
#     print("printing employeee information after unpickling")
#     obj.display()
