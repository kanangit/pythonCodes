#! /usr/bin/env python3

"""
problem: https://www.hackerrank.com/challenges/divisible-sum-pairs
"""
def divisibleSumPairs(n, k, ar):
    length_Ar = len(ar)
    num_pairs = 0
    for i in range(0,length_Ar - 1):
        for j in range(i+1,length_Ar):
            if( (ar[i] + ar[j]) % k == 0):
                num_pairs += 1
    return num_pairs
print(divisibleSumPairs(5,2,[5,9,10,7,4]))
