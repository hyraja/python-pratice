# modules is a way to reuse the code written by someone else.

# math module
import sys
import calendar
import math
print(math.sqrt(16))  # 4.0
print(math.pow(2, 10))  # 1024.0
# to know all the function available inside one module
print(dir(math))
''' ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin',
'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf',
'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']'''


##################### calendar module ###############################
# import calendar
cal = calendar.month(2021, 1)
print(cal)
'''     January 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31 '''
# check the year is a loop year or not
print(calendar.isleap(2020))  # True

############################## sys module ##############################
# if you want to set path of your current location
sys.path.append('D:\Workspace\pratice@Python')
