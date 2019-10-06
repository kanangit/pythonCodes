#1 /usr/bin/env python3
"""
In the case of the array of intgers, the unfairness will be minimal
for the contiguos sorted array. So we must first sort the array, 
and then select the part of it, which has mimimum unfairness
"""
input_arr = []
filename = 'input07.txt'
with open(filename) as f:
    for line in f:
        input_arr.append(int(line))

nom_elements = input_arr.pop(0)
subArr_len = input_arr.pop(0)
print('nom_elements =', nom_elements)

def maxMin(k, arr):
    retVal = 10**9 
    sarr = sorted(arr)
    def get_unfair(arr):
        return arr[len(arr)-1] - arr[0]
    lena = len(arr)
    print('lena =',lena)
    print('k =', k)
    end_range = lena - k + 1
    print('end_range = lena - k + 1 = ',end_range)
    for i in range(0, end_range):
        if (i % 1000 == 0):
            print('i =',i)
        subArr = sarr[i: i + k]
        unf = get_unfair(subArr)
        if (unf < retVal):
            retVal = unf
    return retVal

#myList = [9,8,45,13,84,6,2,1]
#k = 3
myList = input_arr
k = subArr_len
print(maxMin(k,myList))
