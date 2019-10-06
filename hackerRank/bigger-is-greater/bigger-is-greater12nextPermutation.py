#! /usr/bin/env/ python3
from itertools import permutations
def biggerIsGreater(w):
    p = permutations(w)
    while True:
        it = next(p, None)
        if ''.join(list(it)) == w:
            break
    it = next(p, None)
    if (it == None):
        return None
    else:
        return ''.join(it)
print(biggerIsGreater('abcd'))
