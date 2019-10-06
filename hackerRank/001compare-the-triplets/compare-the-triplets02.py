#! /usr/bin/env python3
def sum(slist):
    total = 0
    for x in slist:
        total += x
    return total
def compareElement(a,b):
    retval = [0,0]
    if a > b :
        retval[0]=1
        retval[1]=0
    if b > a :
        retval[0] = 0
        retval[1] = 1
    if a == b:
        retval[0] = 0
        retval[1] = 0
    return retval
def compareTriplets(a,b):
    gradesA = [0,0,0]
    gradesB = gradesA
    for i in range(0,3):
        gradesElem = compareElement(a[i],b[i])
        gradesA[i] = gradesElem[0]
        gradesB[i] = gradesElem[1]
        print('gradesA =', gradesA)
        print('gradesB = ', gradesB)
    finalRetval = [sum(gradesA),sum(gradesB)]
    return finalRetval 
myAdkaz = compareTriplets([17,28,30],[99,16,8])
print(myAdkaz)
