#! /usr/bin/env python3

def kangaroo(x1, v1, x2, v2):
    if (v2 != v1):
        meetingTime = (x1 - x2) / (v2 - v1)
        q, r = divmod(meetingTime, 1)
        if (meetingTime >= 0 and r == 0):
            return "YES"
        else:
            return "NO"
    elif (v2 == v1 and x2 == x1):
        return "YES"
    else:
        return "NO"

x1 = 43
v1 = 2
x2 = 70
v2 = 1

print(kangaroo(x1,v1,x2,v2))
