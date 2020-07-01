# guessing game++++++++++++++++++++++++


from random import randint
import sys
# generate a number 1~10
first = int(sys.argv[1])
last = int(sys.argv[2])
answer = randint(first, last)

# input from user?

# check that input is a number 1~10
while True:
    try:
        ''' we can cheat this way '''
        # print(answer)
        guess = int(input(f'guess a number between {first} to {last}:  '))
        if first < guess < last:
            if guess == answer:
                print(' you are a genius !!! ')
                break
        else:
            print(f'hey bozo, I said {first} ~ {last} ')
    except ValueError:
        print('please enter a number ')
        continue
# check if number is the right guess .otherwise ask again.


#################@@@@@@@@@@@@@@@@@@@@@@@######################

# python package index

''' Find, install and publish Python packages
     with the Python Package Index '''
''' https://pypi.org/ '''
