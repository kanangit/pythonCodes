#! /usr/bin/env/ python3

def roundGrade(grade):
    if (grade > 40):
        gs = str(grade)
        print(gs[1])
    if (grade < 40):
        rgrade = grade
    return rgrade

ret = roundGrade(48)
