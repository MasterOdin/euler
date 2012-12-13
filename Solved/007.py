'''
Problem 7:
    By listing the first six prime numbers: 
        2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10,001st prime number?
    
Solution:
    104743
'''

import time, math

s = time.time()

primeCount = 6
primeCheck = 13

found = False
prime = True

while not found:
    primeCheck += 2
    prime = True
   
    for i in range(3,math.ceil(primeCheck/2),2):
        if primeCheck % i == 0:
            prime = False
            break;
    
    if prime:
        primeCount += 1
    
    if primeCount == 10001:
        found = True

print(str(primeCount) + " prime is " + str(primeCheck))       
print(time.time() - s)