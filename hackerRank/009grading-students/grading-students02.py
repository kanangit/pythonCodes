#! /usr/bin/env/ python3

def roundGrade(grade):
    if (grade > 40):
        gs = str(grade)
        units = int(gs[1])
        tens =int( gs[0])
        print(units)
        print(tens)
        if (units <= 5):
            if ( 5 - units <= 
        rgrade = tens * 10 + units
    if (grade < 40):
        rgrade = grade
    return rgrade


ret = roundGrade(48)
print(ret)
