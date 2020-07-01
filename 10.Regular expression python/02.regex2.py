

# import re
# pattern = re.compile(r"([a-zA-Z]).([a])")

# string = 'search this inside of text please! rajaprasad'

# a = pattern.search(string)

# print(a.group(2))


##############################################################
# check for any mail using regex
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'abababab@gmail.com'

a = pattern.search(string)
print(a)
