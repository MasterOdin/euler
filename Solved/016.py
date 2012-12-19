'''
Created on Dec 18, 2012

Problem :
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2**1000?

Solution:
    1366
'''
import time
s = time.time()

'if python didn\'t allow us to brute force this, we would have to use an array'
'to store all digits, and do calculations on that'
calc = 2**1000
total = 0
for i in range(len(str(calc))):
    total += int(str(calc)[i])
    

print("Total: {0}".format(total))
print("Runtime: " + str(time.time()-s))