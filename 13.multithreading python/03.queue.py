''' Inter thread cummunication using # Queue '''
# ========================================

# queue concept is the most enhanced mechanism for inter thread communication
# and share data between threads.

# queue internally has condition and that condition has lock.hence whenever
# we are using Queue we are not worry about synchronization.

# put() put an item into the queue
# get() remove and return an item from the queue.

'''

producer Thread uses put() method to insert data in the queue. Internally 
this method has a logic to acquire the lock before inserting data into queue.
After inserting data lock will be automatically released.

put() method also checks whether the queue is full or not and if queue is full
then the producer thread will entered into waiting state by calling wait() method internally.

consumer thread uses get() method to remove and get data from the queue . internally
this method has logic to acquire the lock before removing data from the queue.
once removal completed then the lock will be released automatically . 

if the queue is empty then consumer thread will entered into waiting state by 
calling wait() method internally. once queue updated with data then the thread 
will be notified automatically 

'''

# Types of Queue

'''1. FIFO(first-in-first-out)'''
# import queue
# q = queue.Queue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)
# while not q.empty():
#     print(q.get(), end=' ')  # 10 5 20 15

''' 2. LIFO(LAST-IN-FIRST-OUT) '''
# import queue
# q = queue.LifoQueue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)
# while not q.empty():
#     print(q.get(), end=' ')  # 15 20 5 10

''' 3.Priority Queue '''
# import queue
# q = queue.PriorityQueue()
# q.put(10)
# q.put(5)
# q.put(20)
# q.put(15)
# while not q.empty():
#     print(q.get(), end=' ')  # 5 10 15 20
