'''
Created on May 21, 2013

Problem 018:
    By starting at the top of the triangle below and moving to adjacent 
    numbers on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    Solution:
        1074
'''
import time
s = time.time()

L = []
L.append("75")
L.append("95 64")
L.append("17 47 82")
L.append("18 35 87 10")
L.append("20 04 82 47 65")
L.append("19 01 23 75 03 34")
L.append("88 02 77 73 07 63 67")
L.append("99 65 04 28 06 16 70 92")
L.append("41 41 26 56 83 40 80 70 33")
L.append("41 48 72 33 47 32 37 16 94 29")
L.append("53 71 44 65 25 43 91 52 97 51 14")
L.append("70 11 33 28 77 73 17 78 39 68 17 57")
L.append("91 71 52 38 17 14 91 43 58 50 27 29 48")
L.append("63 66 04 68 89 53 67 30 73 16 69 87 40 31")
L.append("04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

M = [i.split(" ") for i in L]
M = [[int(j) for j in i] for i in M]

for i in range(len(M)-2,-1,-1):
    for j in range(0,i+1):
        add = max(M[i+1][j],M[i+1][j+1])
        M[i][j] = M[i][j] + add
        
print(M[0][0])
print("Runtime: " + str(time.time()-s))