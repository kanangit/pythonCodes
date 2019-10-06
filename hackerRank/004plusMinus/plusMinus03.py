#! /usr/bin/env/ python3
sample = [11,12,-321,0,23,-1,32,33]
#print('List size is', len(sample))
#print(sample[1][1])


def plusMinus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    all =float(len(arr))

    for x in arr:
        if x > 0:
          positive += float(1)
        if x < 0:
          negative += float(1)
        if x == 0:
          zeroes += float(1)
    print(positive / all)
    print(negative / all)
    print(zeroes / all)
    return [positive / all, negative / all, zeroes / all]

errorCode = plusMinus(sample)
print(errorCode)
