#1 /usr/bin/env python3
"""
In the case of the array of intgers, the unfairness will be minimal
for the contiguos sorted array. So we must first sort the array, 
and then select the part of it, which has mimimum unfairness
"""
import functools
filename = 'input07.txt'
with open(filename) as f:
    input_arr = list(map(int, f.readlines()))

nom_elements = input_arr.pop(0)
subArr_len  = input_arr.pop(0)
print('nom_elements =', nom_elements)

def maxMin(k, arr):
    arr = sorted(arr)
    shiftedArr = arr[k-1:]
    retVal = min([a - b for a, b in zip(shiftedArr,arr)])
    return retVal

#myList = [9,8,45,13,84,6,2,1]
#k = 3
myList = input_arr
k = subArr_len
print(maxMin(k,myList))



