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
    gradesB = [0,0,0]
    for i in range(0,3):
        gradesElem = compareElement(a[i],b[i])
        gradeAi = gradesElem[0]
        gradeBi = gradesElem[1]
        gradesA[i] = gradeAi
        gradesB[i] = gradeBi
#        print('i =',i)
#        print('a[i]=, b[i]=', a[i],b[i])
#        print('gradesElem=',gradesElem)
#        print('gradeAi =',gradeAi)
#        print('gradeBi =',gradeBi)
#        print('gradesA[0]=',gradesA[0])
#        print('gradesA[1]=',gradesA[1])
#        print('gradesA[2]=',gradesA[2])
#        print('a[i]=, b[i]=', a[i],b[i])
#        print('gradesElem=',gradesElem)
#        print('gradesA[i] = ', gradesA[i])
#        print('gradesElem[0]=',gradesElem[0])
#        print('gradesA =', gradesA)
#        print('gradesB = ', gradesB)
    finalRetval = [sum(gradesA),sum(gradesB)]
    return finalRetval 
myAdkaz = compareTriplets([17,28,30],[99,16,8])
print(myAdkaz)
