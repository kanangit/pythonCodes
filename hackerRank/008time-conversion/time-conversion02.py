#! usr/bin/env/ python3

def timeConversion(s):
    sHours = s[0:2]
    sIndicator = s[8]
    if sIndicator == 'P' and sHours != '12':
        sHours = str(int(sHours) + 12)
    if sIndicator == 'A' and sHours == '12':
        sHours = '00'
    military = sHours + s[2:8]

    return military
x = timeConversion('12:20:30AM')
print(x)
