#! usr/bin/env/ python3

def timeConversion(s):
    sHours = s[0:2]
    sIndicator = s[8]
    if sIndicator == 'P':
        sHours = str(int(sHours) + 12)
    military = sHours + s[2:8]

    return military
x = timeConversion('10:20:30PM')
print(x)
