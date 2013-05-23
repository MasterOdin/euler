'''
Created on May 23, 2013

Problem 028:
    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
    formed in the same way?

Solution:
    669171001

Note:
    Brute-force method. 028_2.py is a more mathematical approach and is faster
'''
import time
s = time.time()
total = 0

dim = 1001
M = [[None] * dim for i in range(dim)]
value = dim**2
x = dim-1
y = 0
directionX = -1
changeX = 0
directionY = 0
changeY = -1

while value > 0:
    M[y][x] = value
    value = value - 1
    change = False

    if not ((x+directionX) >= 0 and (x+directionX) < dim and
            (y+directionY) >= 0 and (y+directionY) < dim and
            M[(y+directionY)][(x+directionX)] == None):
        t = directionX
        directionX = (changeX*-1)
        changeX = t
        t = directionY
        directionY = changeY*-1
        changeY = t

    x = x + directionX
    y = y + directionY

for i in range(0,dim):
    total = total + M[i][i]
    total = total + M[i][(dim-1)-i]

total = total - 1
print(total)

print("Runtime: " + str(time.time()-s))
