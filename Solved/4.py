'''
Problem 4:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

Solution:

'''

def isPalindrome(number):
    ans = str(number)
    return ans == ans[::-1]

maxP = 0
minJ = 99
for i in range(999,99,-1):
    if i*i < maxP:
        break
    for j in range(i,minJ,-1):
        if isPalindrome(i*j) == True:
            print(str(i) + " * " + str(j) + " = " + str(i*j))
            if(maxP < i*j):
                maxP = i*j
                minJ = j
                
print(maxP)