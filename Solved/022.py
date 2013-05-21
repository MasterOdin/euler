'''
Created on May 21, 2013

Problem 022:
    Using Data/022.txt, a 46K text file
    containing over five-thousand first names, begin by sorting it into 
    alphabetical order. Then working out the alphabetical value for each name, 
    multiply this value by its alphabetical position in the list to obtain a 
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which 
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
    COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?

Solution:
    871198282
'''
import time
s = time.time()
total = 0

f = open("../Data/022.txt")
for line in f:
    temp = line
M = temp.split(",")
for i in range(0,len(M)):
    M[i] = M[i].replace('"','')
M.sort()

for i in range(0,len(M)):
    subtotal = 0
    for j in M[i]:
        subtotal = subtotal + (ord(j)-64)
    total = total + subtotal*(i+1)

print(total)
print("Runtime: " + str(time.time()-s))