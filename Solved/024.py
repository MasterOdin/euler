'''
Created on May 22, 2013

Problem 024:
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
s = time.time()
total = 0

def swap(number,i,j):
    k = number[i]
    number[i] = number[j]
    number[j] = k
    return number

number = [0,1,2,3,4,5,6,7,8,9]
numPerm = 1000000
N = len(number)
count = 1
while count < numPerm:
    i = N-1
    while number[i-1] >= number[i]:
        i = i - 1

    j = N
    while number[j-1] <= number[i-1]:
        j = j - 1

    number = swap(number,i-1,j-1)
    i = i + 1
    j = N
    while i < j:
        number = swap(number,i-1,j-1)
        i = i + 1
        j = j - 1
    count = count + 1

print(number)

print("Runtime: " + str(time.time()-s))
