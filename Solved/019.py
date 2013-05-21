'''
Created on May 21, 2013

Problem 019:
    You are given the following information, but you may prefer to do some 
    research for yourself.

    - 1 Jan 1900 was a Monday.
    - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, but not on a century 
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth 
    century (1 Jan 1901 to 31 Dec 2000)?

    Solution:
        171
'''
import time
s = time.time()

days = [31,28,31,30,31,30,31,31,30,31,30,31]
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# let's assume Monday = 0, Sunday = 6
currentDay = 1
total = 0
for i in range(1901,2001):
    for j in range(0,12):
        if currentDay == 6:
            total = total + 1
        if days[j] == 31:
            factor = 3
        elif days[j] == 30:
            factor = 2
        else:
            if (i % 100 != 0 and i % 4 == 0) or (i % 100 == 0 and i % 400 == 0):
                factor = 1
            else:
                factor = 0
        currentDay = currentDay + factor
        if currentDay > 6:
            currentDay = (currentDay-7)
            
print(total)
print("Runtime: " + str(time.time()-s))