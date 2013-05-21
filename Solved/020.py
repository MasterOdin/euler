'''
Created on May 21, 2013

Problem 020:
    n! means n  (n  1)  ...  3 x 2 x 1

    For example, 10! = 10 x 9  ...  3 x 2 x 1 = 3628800,
    and the sum of the digits in the number 10! is 
        3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

Solution:
    171

Note:
    In another language (say C++), the answer to this would involve
    having to seperate out the factorial when it exceeds the maximum value of
    unsigned long at 4,294,967,295. You'd then have to do the multiplication on
    the lower number, and carry the overflow to the larger number as necessary.
    At the end, you'd have broken up the number into 2.1729202e+148 chunks. A
    helper function would be necessary to handle this then. Python however is
    happy to deal with 158 character long integers though so no need.
'''
import time
s = time.time()

import math

totalS = str(math.factorial(100))
print(int(totalS)/4294967295)
print(len(totalS))
total = 0
for i in totalS:
    total = total + int(i)

print(total)
print("Runtime: " + str(time.time()-s))