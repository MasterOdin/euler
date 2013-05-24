'''
Created on May 23, 2013

This is a more mathematical approach to the problem. We know that the edge
contains n numbers (where n is the dimension of the spiral), and we have four
edges. The next four edges will have n-2 numbers, and then the next four will
have n-4 till we have n-i = 1, where we break, and then add 1 to total, where
we get our wanted answer.

Problem 028 (2):
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11`
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
    formed in the same way?

Solution:
    669171001
'''
import time
s = time.time()
total = 0

dim = 1001
value = dim**2
count = 0
subtract = dim-1
while value > 1:
    total = total + value
    value = value - subtract
    count = count + 1
    if count == 4:
        subtract = subtract - 2
        count = 0
total = total + 1

print(total)

print("Runtime: " + str(time.time()-s))
