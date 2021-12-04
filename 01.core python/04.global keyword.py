total = 0

def count():
     global total
     total += 1
     return total
count()
count()
print(count()) #3 

# there is an way to get the same answer
total = 0
def count2(total):
    total += 1
    return total
print(count2(count2(count2(total)))) #3 we are accessing the global variable total and also run this function 3 times and get the out put as 3
