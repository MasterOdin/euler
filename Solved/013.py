'''
Created on Dec 13, 2012

Problem 13:
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
        <See Data/013.txt>

Solution:
    5537376230
    
(I'm guessing this is supposed to be clever usage of splitting numbers to avoid
BIG INTS, but uh...python doesn't care?)
'''

import time
s = time.time()

f = open("../Data/013.txt")
solve = 0

for line in f:
    solve += int(line.split("\n")[0])

print(str(solve)[:10])

print("Runtime: {0}".format(time.time()-s))