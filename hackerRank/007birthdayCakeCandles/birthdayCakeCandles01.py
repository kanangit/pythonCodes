#! /usr/bin/env/ python3
def birthdayCakeCandles(ar):
    ilook = max(ar)
    counter = 0
    for x in ar:
        if x == ilook:
            counter += 1
    return counter
retval = birthdayCakeCandles([1,2,3,4,5,6,7,8,46,1,-100,46,5,30,46])
print(retval)

