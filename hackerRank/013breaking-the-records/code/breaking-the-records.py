#! /usr/bin/env python3
"""
problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

"""
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    n_mins = 0
    n_max = 0
    for x in scores:
        if x < minimum:
            n_mins = n_mins + 1
            minimum = x
        if x > maximum:
            n_max = n_max + 1
            maximum = x 
    return [n_max, n_mins]
print(breakingRecords([1, 2, 3, 4, 5]))