#! /usr/bin/env/ python3

import math

def roundGrade(grade):
    if (grade >= 38):
        nextmultiple = 5 * math.ceil(float(grade) / float(5))
        if (nextmultiple - grade <= 3):
            rgrade = nextmultiple
        else:
            rgrade = grade

    if (grade < 38):
        rgrade = grade
    return rgrade

def gradingStudents(grades):
    for grade in grades:
        grade = roundGrade(grade)
    return grades
listofgrades = [38,48,63,52,41,99]
ret = gradingStudents(listofgrades)
print(ret)
