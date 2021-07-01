# we need to adding each digits of a number
# 576 => 5+7+6 = 18 => 1+ 8 = 9

# x = int(input('enter a number : '))  # 576
# sum_digit = 0
# sum_of_digits = 0
# for digit in str(x):
#     sum_digit += int(digit)
#     print(sum_digit, end=' ')
# for digit in str(sum_digit):
#     sum_of_digits += int(digit)
#     # print(sum_of_digits, end=' ')
# print(f'sum of each digits is {sum_of_digits}')
# enter a number : 576
# 5 12 18 sum of each digits is 9

# or compact way
number = 576

sum_of_digits = sum(int(digit) for digit in str(number))
sum_digit = sum(int(digit) for digit in str(sum_of_digits))
print(sum_digit)  # 9
