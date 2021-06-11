# requests-module
# https://pypi.org/project/requests/

# SHA1-generator
# https://passwordsgenerator.net/sha1-hash-generator/

# Pwned-Passwords
# https://haveibeenpwned.com/Passwords

# we don't need to provide whole SHA1 character bcz
# someone can guess the password
# so we use a technique [K-Anonimity]--> this is a modern
# technique to track user without knowing who you are and
# this technique widely used in industry standard.

# we use this technique as , not provide whole SHA1 character
# only provide the first 5 character of our hashed password
# this api should check all password with first 5 character matched using this
# way we can able to keep safe . and also gives us result.

import requests
import hashlib
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)  # <Response [200]>


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching :{res.status_code}, check the api and try again')
    return res


def pwned_api_check(password):
    # check password if it exists in api response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char, tail)
    return sha1password


pwned_api_check('123')
