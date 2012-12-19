'''
Created on Dec 13, 2012

Problem 012:
    The sequence of triangle numbers is generated by adding the natural numbers. 
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The 
    first ten terms would be:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:
         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28
        36: 1,2,3,4,6,6,9,12,18,36
        45: 1,3,5,9,15,45



 
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?

Solution:
    76576500
'''
import time
s = time.time()

factorExponent = 0
triangleNum = 7
triangleSum = 28
found = False
factors = []
while not found:
    triangleNum += 1
    triangleSum += triangleNum
    factorExponent = 0
    
    temp = triangleSum
    factors[:] = []
    
    numOfDivisors = 1
    
    while temp % 2 == 0:
        factorExponent += 1
        temp /= 2
    
    if factorExponent > 0:    
        factors.append(factorExponent)
    
    divisor = 3
    stillFactor = True
    
    while stillFactor == True:
        factorExponent = 0
        while temp % divisor == 0:
            factorExponent += 1
            temp /= divisor
        if factorExponent > 0:
            factors.append(factorExponent)
        
        if(temp == 1):
            stillFactor = False
        else:
            divisor += 2
    

    for i in factors:
        numOfDivisors *= (i+1)
        
    if(numOfDivisors >= 499):
        found = True


print('Triangle number {0} has a sum of {1} and >= 500 divisors with {2} divisors'.format(triangleNum,triangleSum,numOfDivisors))

print("Runtime: " + str(time.time()-s))