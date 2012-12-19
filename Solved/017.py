'''
Created on Dec 18, 2012

Problem 017:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
    in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
    20 letters. The use of "and" when writing out numbers is in 
    compliance with British usage.  

Solution:
    21124
'''
import time
s = time.time()
numDic = {
     0:"",
     1:"one", 
     2:"two", 
     3:"three",
     4:"four",
     5:"five",
     6:"six",
     7:"seven",
     8:"eight",
     9:"nine",
     10:"ten",
     11:"eleven",
     12:"twelve",
     13:"thirteen",
     14:"fourteen",
     15:"fifteen",
     16:"sixteen",
     17:"seventeen",
     18:"eighteen",
     19:"nineteen",
     20:"twenty",
     30:"thirty",
     40:"forty",
     50:"fifty",
     60:"sixty",
     70:"seventy",
     80:"eighty",
     90:"ninety",
     100:"hundred",
     1000:"thousand" 
     }

def get_word_count(i):
    """get word count of written number names. works for i < 10**5""" 
    if i/19 < 1:
        return len(numDic[i])
    elif i < 10**2:
        return len(numDic[i%10])+len(numDic[(i-(i%10))])
    elif i < 10**3:
        if i % 100 == 0:
            return len(numDic[i/100])+len(numDic[100])
        else:
            return len(numDic[int(i/100)])+len(numDic[100])+3+get_word_count(i%100)
    elif i < 10**4:
        return len(numDic[int(i/1000)])+len(numDic[1000])+get_word_count(i%1000)
    else:
        return 0
        


total = 0

for i in range(1001):
    total += get_word_count(i)
    
print(total)

print("Runtime: " + str(time.time()-s))