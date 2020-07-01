# Password Validator

# atleast 8 char long.
# contain any sort letters, numbers $%#@
# has to end with a number

import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

password = 'supersecrete%5'

c = pattern.fullmatch(password)

print(c)
