'''
Problem 3:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

Solution:
    6857
'''

num = 600851475143

factor = 3

while(num > 1):
    if(num % factor == 0):
        num /= factor
    else:
        factor += 2


print(factor)
        