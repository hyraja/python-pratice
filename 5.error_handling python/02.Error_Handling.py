# Error Handling

# error handling means to continue our program if there are  errors not to crash our programe .

# while True:
#     try:
#         age = int(input("enter your age ?"))
#         print(f'your age is {age}')
#     except:
#         print("please enter a  number ")
#     else:
#         print("thank you")
#         break

# ++++++++++++++++++++++++++++++++++++
while True:  # it is use for infinity loop.
    try:
        age = int(input('what is your age? '))
        print(10/age)
    except ValueError:
        print('please enter a number ')
    except ZeroDivisionError:
        print('please enter a age higher than 0')
    else:
        print('Thank you')
        break
''' if 2 valueerror in except block  available, python only take 1st one .
