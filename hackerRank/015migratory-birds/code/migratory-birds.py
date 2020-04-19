#! /usr/bin/env python3

"""
problem: https://www.hackerrank.com/challenges/migratory-birds/problem
"""

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a_freqs = [0]*5
    for bird in arr:
        a_freqs[bird-1] += 1
        max_freq = max(a_freqs)
    for i in range(0,len(a_freqs)):
        if (a_freqs[i] == max_freq): return i + 1

print(migratoryBirds([1,2,3,3,3,3,4,1,1,1,2,2,3,3]))
