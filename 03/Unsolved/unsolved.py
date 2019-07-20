#!/usr/bin/python3
from helpers import *
# BRIEF //
#   The student script from last time was a good first-pass. Now, it's time to
#   make it a bit more robust.
#
#   To start, refactor such that all of your prompts occur within a loop, which
#   doesn't break until the user indicates the information they entered is 
#   correct. Only print the information after their confirmation.
#
#   Next, refactor your program such that, after users confirm that they've
#   entered the correct information, your program prompts them as to whether 
#   they'd like to enter information for additional students.
#   
#     1. As an "easy" challenge, simply allow them to enter the values again,
#        and print the information after they confirm it's correct.
#
#     2. Your recommended challenge is to store student information in a dict,
#        and create a new one for each student the user adds. Store these
#        students in a list, and print the entire list when the user declines
#        to add additional students.


# "Global" students list.
students = []

while True:
# Student Information Function
    first, middle, last, address, email, phone = studentInformation() 

# Creating student
    student = createStudent(firstName = first, middleName = middle, lastName = last, address = address, email = email, phone = phone)

#printing student
    printStudent(student)

#prompts for confirmation
    if confirm('Is this information correct ? (Y/N)'):
        students.append(student)
        if confirm('Would you like to input another student ? (Y/N)'):
            continue
        else:
            printSummary(students)
            break
