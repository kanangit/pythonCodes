#! /usr/bin/env/ python3

n = 6

def staircase(n):
    for i in range(1,n + 1):
        print(' '*(n - i) + '#' * i)
    return 0
retval = staircase(n)

