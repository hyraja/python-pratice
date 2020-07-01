# debugging in python

''' tha act of finding and removing errors/exceptions are called debugging. '''

# linting: allow us to find error before run the code


# pdb is built-in module for debugging

import pdb


def add(num1, num2):

    pdb.set_trace()
    return num1+num2


add(4, 'raja')

'''
-> return num1+num2
(Pdb) num1
4
(Pdb) num2
'raja'
(Pdb)  '''

''' different command available in python like

(pdb) help # it gives all info about pdb
(pdb) list # it gives list of my code
(pdb) help list #list source code for current file 
(pdb) step # it going to change cursor next line
(pdb) a # gives all the arguments
(pdb) w # contexts of current line
(pdb) next # gives next line content
(pdb) exit# to exit
'''
# after figuring error fix the code and remove debugger
