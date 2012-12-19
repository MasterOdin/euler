'''
Created on Dec 18, 2012

Problem 14:
    The following iterative sequence is defined for the set of positive integers:
        n -> n/2 (n is even)
        n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

Solution:
    837799
'''
import time
s = time.time()

a = {}

start = 0
count = 0
maxCount = 1
maxNum = 0
tmpTotal = 0

for i in range(1,1000000):
    start = i
    count = 1
        
    while start > 1:
        if start not in a: 
            if start%2 == 0:
                start /= 2
            else:
                start = 3*start+1
        
            count += 1
        else:
            count += a[start]
            start = 1
    
    a[i] = count
    
    if count > maxCount:
        print("Got {0} chain steps on number '{1}'".format(count,i))  
        maxCount = count
        maxNum = i
        
print("MAXIMUM: Got {0} chain steps on number '{1}'".format(maxCount,maxNum))   
print("Runtime: " + str(time.time()-s))