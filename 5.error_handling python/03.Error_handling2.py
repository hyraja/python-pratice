# Error handling


def sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        print(f"please enter number and error is  '{err}'")


print(sum(1, 2))  # 3

# we can wrap multiple error at a time for handling


def div(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:  # we wrap 2 errors at a time
        print('enter number and number > 0')
        print(err)


''' for str  err o/p unsupported operand type(s) for /: 'int' and 'str' '''
''' for 0 err o/p division by zero '''

print(div(1, '9'))  # enter number and number >0
print(div(1, 0))  # enter number and number >0

#######################################++++++++++++++++++++#########################

''' try -> except -> else -> finally '''


while True:
    try:
        age = int(input("enter your age? "))
        10/age
    except ValueError:
        print("please enter a number")
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you')
        break
    # finnaly used when all the things done in above block
    finally:
        print("ok, i am finally done. ")
print("can you hear me ?")

''' 
enter your age? 5
thank you
ok, i am finally done.
can you hear me ? '''

# 'finally' used when you want to login but giving the wrong password
# multiple time , how much time of  finally execute that much of
# time user want to login. finally used for loging purposes.
