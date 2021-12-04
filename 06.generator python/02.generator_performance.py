from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'time taken is {t2-t1}s')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for item in range(10000000):
        item*5


@performance
def long_time2():
    print('2')
    for item in list(range(10000000)):
        item*5


long_time()  # time taken is 0.8320925235748291s ' it is a generator'
long_time2()  # time taken is 0.9163656234741211s' it is an iterable'

''' generators are faster thhan normal itarators
    so it is useful when calculating large amount of data '''
    
