'''
Created on May 22, 2013

This program attempts to solve the problem through mathematics instead of brute
forcing the problem. It's based around knowing that the first number has 9!
permutations for the other spots, the second number has 8! and so on and so 
forth. We then grab whatever the number is at the index specified by the
number of times the factorial goes into the remaining number, and we get our
answer

Problem 024 (2):
    A permutation is an ordered arrangement of objects. For example, 3124 is 
    one possible permutation of the digits 1, 2, 3 and 4. If all of the 
    permutations are listed numerically or alphabetically, we call it 
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 
    4, 5, 6, 7, 8 and 9?

Solution:
    2783915460
'''
import time
from math import factorial
s = time.time()
total = 0

number = [0,1,2,3,4,5,6,7,8,9]
printN = [0,1,2,3,4,5,6,7,8,9]
numPerms = 1000000-1
digit = 0
N = len(number)
for i in range(1,len(number)):
    j = int(numPerms/factorial(N-i))
    numPerms = numPerms % factorial(N-i)
    printN[(i-1)] = number[j]
    number.pop(j)
    if numPerms == 0:
        break

for j in range(i,N):
    printN[j] = number[0]
    number.pop(0)

print(printN)

print("Runtime: " + str(time.time()-s))
