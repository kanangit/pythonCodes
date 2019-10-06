#! /usr/bin/env python3
"""
problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""
import functools
def birthday(s, d, m):
    def is_amatch(sl):
        return int(sum(sl) == d)
    indSlices = [slice(i, i + m, 1) for i in range(len(s))]
    
    return sum(map(is_amatch, [s[ind] for ind in indSlices]))
print(birthday([1, 2, 1, 3, 2],3,2))