# Read Write Append

# we can use with statement and don't worry about close()

# mode = 'r' default
# mode = 'w' write
# mode = 'r+' read and write
# mode = 'a' append

with open('02.readwrite.txt', mode='a') as my_file:

    ''' we want to write in file so
       we specify mode='w' inside 'test.txt' '''

    text = my_file.write(':)')
    print(text)
# if we write something cursor reset and another we write it's overwrite

# write also create a file when it doesnot exist or override ..
with open('02.sad.txt', mode='w') as f:
    text = f.write(':(')
    print(text)  # 02.sad.txt file is not available write mode create it


# path library in python
    ''' https://docs.python.org/3/library/pathlib.html '''


###########################################################
# Avoid file errors in python
###########################################################

try:
    with open('02.sad.txt', mode='r') as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print('file doesnot exist')
    raise err
except IOError as err:  # if we are giving not supported mode we can see these error.
    print('IO error')
    raise err
