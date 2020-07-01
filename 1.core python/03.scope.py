# SCOPE ---->what variable do i have access to
# python uses function scope.
a = 5


def confusion():
    a = 10
    return a


print(a)  # 5
print(confusion())  # 10

# scope rules :::::::::(LGBT rule)-->local global builtin
# 1. start with local
# 2. parent local?
# 3. Global
# 4. built in python functions.
# 5.

# why use scope?
# ans : with the help of scope we are pointing to our programme to fighure out, where are our variables are located.
# using nonlocal keyword we are recall the global variable and use it so it helps to minimize memory consumption.
