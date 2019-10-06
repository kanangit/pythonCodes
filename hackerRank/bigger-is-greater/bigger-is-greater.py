#! /usr/bin/env/ python3
from itertools import permutations
def biggerIsGreater(w):
    tupel = tuple(w)
    myIterable = ''.join(sorted(w)) # In order for the permutations to return the 
# result in lexicographical order the input iterable should be sorted
    p = permutations(myIterable)
    plist = list(p)
    indNextSmallest = plist.index(tupel) + 1
    if (indNextSmallest + 1) > len(plist):
        return 'no answer'
    elif (plist[indNextSmallest] == tupel):
            return 'no answer'
    else:
        return ''.join(plist[indNextSmallest])

print(biggerIsGreater('dkhc'))
