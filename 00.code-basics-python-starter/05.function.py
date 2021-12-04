# ----------------------------------------------
# 1. function intro
# 2. function arguments and return value
# 3. Default Arguments
# 4. Local vs Global variable
# 5. Documentation strings
# ------------------------------------------------

# function is a block of code that perform a specific task.

# find out expens of 2 friend
# ----------------------------------
# def calculate_expenses(exp):
#     total = 0
#     for item in exp:
#         total = total+item
#     return total


# toms_expenses = [20000, 202020, 3000]
# joes_expenses = [30303030, 708080]

# tom_exp = calculate_expenses(toms_expenses)
# joe_exp = calculate_expenses(joes_expenses)

# print(f'tom\'s expenses {tom_exp}')
# print(f'joe\'s expenses {joe_exp}')

# find out sum of 2 number
total = 0


def sum(a, b=0):
    ''' this function take one input compulsory and another one is a default value 0 , and then
    it adds the 2 number'''
    print('a :', a)
    print('b :', b)

    total = a+b
    print(f'total inside function {total}')
    return total


num = sum(40, 80)
print(f'Total outside function {num}')
print(total)
