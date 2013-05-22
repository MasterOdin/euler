'''
Created on May 22, 2013

Problem 025:
    The Fibonacci sequence is defined by the recurrence relation:
        Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:
        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144
    
    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?

Solution:
    2783915460
'''
import time
s = time.time()
total = 0
def fibonacci():
    a = 0
    b = 1
    count = 0
    while len(str(b)) < 1000:
        t = b
        b = a + b
        a = t
        count = count + 1

    count = count + 1
    return count

print(fibonacci())


print("Runtime: " + str(time.time()-s))
