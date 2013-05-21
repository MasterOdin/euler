'''
Created on May 21, 2013

Problem 023:
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors 
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
    number.

    A number n is called deficient if the sum of its proper divisors is less 
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
    number that can be written as the sum of two abundant numbers is 24. By 
    mathematical analysis, it can be shown that all integers greater than 28123 
    can be written as the sum of two abundant numbers. However, this upper limit 
    cannot be reduced any further by analysis even though it is known that the 
    greatest number that cannot be expressed as the sum of two abundant numbers 
    is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum 
    of two abundant numbers.

Solution:
    4179871
'''
import time
from math import sqrt
s = time.time()
total = 0

def d(n):
    temp = 1
    t = sqrt(n)
    for i in range(2,(int(t)+1)):
        if n % i == 0:
            temp = temp + i + n/i
    if t == int(t):
        temp = temp - t
    return int(temp)

abd = set()
for i in range(1,28123):
    if d(i) > i:
        abd.add(i)
    if not any((i-a in abd) for a in abd):
        total = total + i


print(total)
print("Runtime: " + str(time.time()-s))