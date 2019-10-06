#! /usr/bin/env/ python3
from itertools import permutations
def biggerIsGreater(w):
    myIterable = ''.join(sorted(w)) # In order for the permutations to return the 
# result in lexicographical order the input iterable should be sorted
    p = permutations(myIterable)
    while True:
        it = next(p, None)
        print(''.join(list(it)))
        if ''.join(list(it)) == w:
            break
    it = next(p, None)
    if (it == None):
        return None
    else:
        if ''.join(list(it)) == w:
            return None
        else:
            return ''.join(it)
print(biggerIsGreater('dkhc'))
