'''
Created on Dec 18, 2012

Problem 15:
    Starting in the top left corner of a 22 grid, there are 6 routes 
    (without backtracking) to the bottom right corner.
            <http://projecteuler.net/project/images/p_015.gif>
    How many routes are there through a 2020 grid?

Solution:
    137846528820
'''
import time,math

def choose(n,k):
    return math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))

s = time.time()

gridSize = 20


print("Total paths: {0}".format(choose(40,20)))

print("Runtime: " + str(time.time()-s))

