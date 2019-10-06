#! /usr/bin/env python
import functools
"""
Calculate how many apples and oranges have fallen on the house,
that Jack built
"""

def countFruits(s, t, a, fruits):
    def is_ontheroof(a,d,s,t):
        if (a + d >= s and a + d <= t):
            return 1
        else:
            return 0

    n_fruits = sum(map(lambda d: is_ontheroof(a,d,s,t),fruits))
    return n_fruts

#    n_apples = sum(map(lambda d: is_apple_ontheroof(a,d,s,t,b),apples))
#    return n_apples
a = 0
b = 7
s = 2
t = 5
d = 1
apples = [1,2,3,4,5]
oranges = [1.5,2.5, 3.5]
print(countApplesAndOranges(s,t,a,b,apples,oranges))
