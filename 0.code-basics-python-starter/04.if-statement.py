# check number is even or odd.

# num = int(input("enter a number:"))

# if num % 2 == 0:
#     print("it is an even number:")

# else:
#     print("it is an odd number")

# ask user to choose cuisine and then it ask which type of cuisine.
indian = ['dal', 'rice', 'nan']
nigerian = ['friend rice', 'pizza']
italian = ['soya pasta', 'fried rice', 'egg role']

dish = input("enter a dish name: ")

if dish in indian:
    print("Indian")
elif dish in nigerian:
    print("nigerian")
elif dish in italian:
    print("italian")
else:
    print(
        f'Based on my knowledge i have, i don\'t know which type of cuisine is {dish}'
    )
