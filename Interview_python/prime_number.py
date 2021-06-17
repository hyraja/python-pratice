# findout prime number

num = int(input('enter a number'))

if num > 1:
    for i in range(2, num+1):
        if (num % i) == 0:
            print(f'{num} is not a prime number')
            break
        else:
            print(f'{num} is a prime number')
else:
    print(f'{num} is  not a prime number')
