'''
Created on Dec 18, 2012

Problem 017:
    If the numbers 1 to 5 are written out in words: one, two, three, four, 
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written 
    out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
    and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
    contains 20 letters. The use of "and" when writing out numbers is in 
    compliance with British usage.  

Solution:
    21124
'''
import time
s = time.time()
a = ["one","two","three","four","five","six","seven","eight","nine","ten", \
     "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty",\
     "thirty","forty","fifty","sixty","seventy","eighty","ninety", "hundred","thousand" ]
andL = 3

onesPlace = 0;
for i in range(0,9,1):
    onesPlace += len(a[i])
    
tens = 0
for i in range(9,19):
    tens += len(a[i])

underH = 0
for i in range(19,27):
    underH += (len(a[i])*10)+onesPlace

underH += tens + onesPlace

hundreds = 0
for i in range(0,9):
    hundreds += (len(a[i])+len(a[27])+3)*100-3+underH
    
total = len(a[0])+len(a[28])+hundreds+underH
    
print(total)

print("Runtime: " + str(time.time()-s))