#! /usr/bin/env python3
"""
https://www.hackerrank.com/challenges/between-two-sets/problem
"""
def getTotalX(a,b):
    startaVal = max(a)
    endaVal = min(b)
    startbVal = min(b)
    endbVal = max(b)

    val = startaVal

    temp_factorA = []
    temp_factorB = []
    factorA = []
    factorAB = []

    for val in range(startaVal,endaVal + 1):
        for x in a:
            if (val % x == 0):
                temp_factorA.append(val)
        if (len(temp_factorA) == len(a)):
            factorA.append(temp_factorA[0])
        temp_factorA = []
    print(factorA)
    for val in factorA:
        for x in b:
            if (x % val == 0):
                temp_factorB.append(val)
        if (len(temp_factorB) == len(b)):
            factorAB.append(temp_factorB[0])
        temp_factorB = []

    return len(factorAB)

a = [2,4]
b = [16,32,96]
sol = getTotalX(a,b)
print(sol)
