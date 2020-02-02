"""problem:
https://www.hackerrank.com/challenges/ctci-bubble-sort/
"""

def countSwaps(a):
    def swap(arr, k,l):
        tmp = arr[k]
        arr[k] = arr[l]
        arr[l] = tmp
        return arr
    
    numSwaps = 0
    oldSwaps = -1
    finalElem = len(a) -1;
    while( numSwaps != oldSwaps):
        oldSwaps = numSwaps
        for j in range(finalElem):
            if a[j] > a[j+1]:
                a = swap(a, j, j+1)
                numSwaps = numSwaps + 1
        finalElem = finalElem - 1

    print('Array is sorted in',numSwaps,'swaps.')
    print('First Element:', a[0])
    print('Last Element:',a[len(a)-1])