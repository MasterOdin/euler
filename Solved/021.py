'''
Created on May 21, 2013

Problem 021:
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).

    If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
    each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

Solution:
    31626
'''
import time
from math import sqrt
s = time.time()
total = 0

nonSum = []
nonInteger = []
amicable = []

def d(n):
    temp = 1
    t = sqrt(n)
    for i in range(2,(int(t)+1)):
        if n % i == 0:
            temp = temp + i + n/i
    if t == int(t):
        temp = temp - t
    return int(temp)

for i in range(2,10000):
    temp = d(i)
    
    if temp in nonInteger:
        index = nonInteger.index(temp)
        if i == nonSum[index]:
            amicable.append(temp)
            amicable.append(i)
            nonInteger.pop(temp)
            nonSum.remove(i)
            continue
    
    nonSum.append(temp)
    nonInteger.append(i)

total = sum(amicable)


print(total)
print("Runtime: " + str(time.time()-s))