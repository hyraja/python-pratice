# MultiThreading


# there are 3 ways of create Thread in python

# 1. Creating Thread without using any class
# 2. Creating Thread by extending Thread class
# 3. creating  Thread without extending Thread class


# 1. creating Thread without using any class
# ==============================================

# from threading import *


# def display():
#     for i in range(1, 11):
#         print('child Thread')


# t = Thread(target=display)  # creating thread object
# t.start()  # starting thread
# for i in range(1, 11):
#     print('Main Thread')


# 2. Creating thread by extending Thread class
# =======================================================

# from threading import *


# class Mythread(Thread):
#     def run(self):
#         for i in range(10):
#             print(f'child thread {i}')


# t = Mythread()
# t.start()
# for i in range(10):
#     print(f'main thread {i}')


# 3. creating Thread without extending Thread class
# ====================================================

# from threading import *


# class Test:
#     def display(self):
#         for i in range(10):
#             print(f'child thread {i}')


# obj = Test()
# t = Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print(f'main thread {i}')

# example
from threading import *
import time


def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double ', 2*n)


def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('squares', n*n)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
beginingtime = time.time()
t1 = Thread(target=doubles, args=(numbers,))
t2 = Thread(target=squares, args=(numbers,))
t1.start()
t2.start()
t1.join()
''' if a thread wants to wait untill completingsome other thread then
we should go for joi nethod '''
t2.join()
print(f'The Total time taken:  {time.time()-beginingtime}')

# we can get thread name by using  current_thread.getName()
print(t1.getName())  # Thread-1

# we can also set our thread name as well using current_thread.setName()
t1.setName('raja')
print(t1.getName())  # raja

# we can also get identification number of thread using current_thread().ident
print(t1.ident)  # 6804

# we can check active threads current running using active_count()
print('the number of active threads ', active_count())


# we can check thread is alive or not usint current_tread.isAlive()
print(t2.name, 'is alive :', t2.is_alive())  # Thread-2 is alive : False
print(t1.name, 'is alive :', t1.is_alive())  # raja is alive : False

# ==============================================
# Daemon Thread
# ==============================================

# The Threads which are running in the background are called daemon Threads.
# the main objective of daemon threads is to provide support for non-daemon
# threads(like Main thread) ex: garbage collector

# we can check the thread is deamon thread or not by isDaemon()
print(t1.isDaemon())  # False

# we can set daemon state(nature) by using setDaemon()
# but before starting of Thread.
print(t1.setDaemon(True))  # it gives error bcz thread already start
# just mindit before starting of thread you need to set value for that.


# ====================================================================
# Synchronization
# ====================================================================
# if multiple threads are executing simultaneously using same class/method  there
# should be chance of data inconsistency problem,
# to overcome this problem synchronization comes in picture

''' in Synchronization the threads will be exeecuted one by one so that
we can overcome data inconsistancy problem
# Syncronization means at a time only one Thread '''

# main application of synchronization are
# 1. online reservation system
# 2. Funds transfer from joint accounts


''' In python, we can implement synchronization by using

   # 1. LOCK (at a time one thread is allowed to execute)

'''
# i = LOCK()
# i.acquire()  # Thread can accure the lock
# i.release()  # Thread release the lock
'''

# 2. RLOCK (at a time one thread is allowed to execute but
      owner can use same lock object multiple time)

'''
i = RLOCK()
i.acquire()
i.release()

'''
               
   # 3. Semaphore (it can be used to limit the access to the shared resources
                   with limited capacity. )

'''
s = Semaphore(counter)
s.acquire()
# for every acquire() call counter value will be decremented.
s.release()
# for every release() call counter value will be Incremented.

s = Semaphore(3)  # in this case semaphore object can be accessed
# by 3 threads at a time. the remaining threads have
# to wait untill releasing the semaphore
'''


'''
