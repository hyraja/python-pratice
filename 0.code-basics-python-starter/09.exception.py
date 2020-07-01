# ---------------------------- TOPICS ---------------------
# 1. what are exceptions.
# 2. Handling an exception.
# 3. Figure out type of exception.
# 4. Handle Multiple exceptoion.
# ----------------------------------------------------------

# Exceptiona are the errors detected at the time of programme executions.

x = int(input('enter a number: '))
y = int(input('enetr anaother number: '))

try:
    z = x/y
except Exception as e:
    print("exception occured ", e)  # exception occured  division by zero
    z = None
print("Division is ", z)  # Division is  None
# using exception handling ... our programme executed without any crash.

# to know type of exceptions occured.
s = input('enter a number: ')
t = input('enter another number: ')

try:
    u = int(s)/int(t)
except ZeroDivisionError:
    print('zero division error')
    u = None
except Exception as e:
    print('exception occured: ', type(e).__name__)
    # exception occured:  TypeError
    # so we know that it is a type error.
    u = None
print('division is ', u)  # division is  None
