'''
Created on May 23, 2013

Problem 026:
    A unit fraction contains 1 in the numerator. The decimal representation of 
    the unit fractions with denominators 2 to 10 are given:

    1/2  =   0.5
    1/3  =   0.(3)
    1/4  =   0.25
    1/5  =   0.2
    1/6  =   0.1(6)
    1/7  =   0.(142857)
    1/8  =   0.125
    1/9  =   0.(1)
    1/10 =   0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can 
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring 
    cycle in its decimal fraction part.

Solution:
    983
'''
import time
s = time.time()
maxD = 0
maxL = 0

for j in range(999,1,-1):
    if maxL >= j:
        break
    L = [0] * j
    position = 0
    temp = 1
    while L[temp] == 0 and temp != 0:
        L[temp] = position
        temp = (temp*10) % j
        position = position + 1
    if position-L[temp] > maxL:
        maxD = j
        maxL = position-L[temp]

print(maxD + " with length of " + maxL)

print("Runtime: " + str(time.time()-s))
