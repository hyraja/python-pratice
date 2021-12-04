# raise our own error.

while True:
    try:
        age = int(input("what is your age? "))
        10/age
        # we can raise any error as we want.
        # raise ValueError('het cut it out')
        raise Exception(' exception happens')
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("thank you")
    finally:
        print('ok, i am done.')

    ''' 
raise ValueError('het cut it out')
ValueError: het cut it out '''

''' 
raise Exception('het cut it out')
Exception: het cut it out '''
