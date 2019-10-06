#! /usr/bin/env/ python3


def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    arrAscending = sorted(arr)
    arrDescending = sorted(arr, reverse = True)
    for i in range(0,len(arr)-1):
        minimum += arrAscending[i]
        maximum += arrDescending[i]
    retString = str(minimum) + ' ' + str(maximum)
    print(retString)
    return retString
rs = miniMaxSum([1,2,3,4,5])

