#! /usr/bin/env/ python3
sample = [[11,12,13],[21,22,23],[31,32,33]]
#print('List size is', len(sample))
#print(sample[1][1])


def diagonalDifference(arr):
    goodDiagonal = 0
    evilDiagonal = 0
    endindex = len(arr)

    for i in range(0,endindex):
        goodDiagonal += arr[i][i]
        evilDiagonal += arr[i][endindex-1-i]
    return abs(goodDiagonal-evilDiagonal)

errorCode = diagonalDifference(sample)
print(errorCode)
