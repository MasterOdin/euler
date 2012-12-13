'''
Problem 5:
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?

Solution:
    232792560
'''

num = 2520
sol = 0

for i in range(10,1,-1):
    if num % i != 0:
        print("failure")
    

found = False

while not found:
    for i in range(19,10,-1):
        if num % i != 0:
            break
        if i == 11:
            found = True
            sol = num

    num += 20

print(sol)
        
        