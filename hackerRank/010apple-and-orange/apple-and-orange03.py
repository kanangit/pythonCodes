#! /usr/bin/env python
import functools
"""
Calculate how many apples and oranges have fallen on the house, 
which was built by Jack
"""

def countApplesAndOranges(s,t,a,b,apples, oranges):
    def is_apple_ontheroof(a,d,s,t,b):
        if (a + d >= s and a + d <= t):
            return 1
        else:
            return 0

    interm_result = is_apple_ontheroof(a,2.5,s,t,b)
    n_apples = sum(map(lambda d: is_apple_ontheroof(a,d,s,t,b),apples))
    return n_apples

a = 0
b = 7
s = 2
t = 5
d = 1
apples = [1,2,3,4,5]
oranges = [1.5,2.5, 3.5]
print(countApplesAndOranges(s,t,a,b,apples,oranges))
