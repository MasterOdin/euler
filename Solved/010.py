'''
Created on Dec 13, 2012

Problem 10:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.  

Solution:
    142913828922
'''
import time,math
s = time.time()

bound = 2000000
sieve = list(None for i in range(bound))

solution = 2

for i in range(3,bound,2):
    if sieve[i] == 2:
        continue
    
    solution += i
    
    for j in range(2,int(math.ceil(bound/i))):
        sieve[i*j] = 2

print(solution)

print("Runtime: {0}".format(time.time()-s))