# Multi tasking(doing multiple things at a time)

# there are are 2 types of multi tasking.
# 1. multithreading based
''' Threads run in the same unique memory heap.'''


# 2. Multiprocessing based
''' Whereas Processes run in separate memory heaps '''

# ========================================================================
''' Multi threading '''
# =======================================================================
''' execution of several task simultaneously where each task is a separate
independent part  of same program  is called muti threading based multitasking
and eaach independent part is called Thread. '''

# example of multithreading:
''' 
     graphics        responding to keystroke    grammercheck
        |                     |                      |
        |=>Thread1            |=>Thread2             |=>Thread3
        |                     |                      |
        ________________(Word Processor)______________
                              | 
                              |
                              |
                             CPU
                        # MultiThreading



# wordprocessor is a application
'''

''' The multithreading library is lightweight, 
shares memory, responsible for responsive UI 
and is used well for I/O bound applications. 
However, the module isn’t killable and is subject to the GIL '''

# The Global Interpretor Lock (GIL) in CPython prevents parallel threads of execution on multiple cores.
# GIL allow us to execute single thread at a time to prvent data collision and


# the main important area of multithreadings
# 1 . To implement multimedia graphics.
# 2 . To develop animations
# 3. to develop video games
# 4 . To develop web and aplication servers

# ==========================================================
# Multiprocessing
# ==========================================================
''' Executing several tasks simmultaneously where each task is a separate process
and also uses separete memory heap is called process based multitasking or multiprocessing '''

# example :
''' while typing python program in the editor we can listen mp3 audio song
from the same system . at the same time we can download a file from internet 
All these tasks are executing simmultaneous;y and independent of each other 
Hence this is process based multitaskng. '''


'''
 
 The multiprocessing library uses separate memory space,
  multiple CPU cores, bypasses GIL limitations in CPython,
   child processes are killable(ex. function calls in program) 
   and is much easier to use. Some caveats of the module are a 
   larger memory footprint and IPC’s a little more complicated 
   with more overhead.
'''

'''

 Though multiprocessing is fundamentally different from the threading library,
  the syntax is quite similar. The multiprocessing library gives 
  each process its own Python interpreter and each their own GIL.
'''
