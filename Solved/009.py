'''
Created on Dec 13, 2012

Problem 9:
    A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
        a^2 + b^2 = c^2
    For example, 
        3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc. 

Solution:
    31875000
'''
import time
s = time.time()

done = False

while not done:
    for a in range(1,499+1):
        for b in range(1,499+1):
            c = (1000-a-b)
            if a**2 + b**2 == c**2:
                print("a("+str(a)+")*b("+str(b)+")*c("+str(c)+") = " + str(a*b*c)) 
                done = True
                break
        if done:
            break

print("Runtime: " + str(time.time()-s))