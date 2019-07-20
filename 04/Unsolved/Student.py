#!/usr/bin/python3

#making student class
class Student:
    #required definitions for students
    def studentInfo(self, first, middle, last, address, email, phone):
        self.first_name = first
        self.middle_initial = middle
        self.last_name = last
        self.address = address
        self.email = email
        self.phone = phone

    def printInfo(self):
        print(self.first_name, self.middle_initial, self.last_name, "\n",
             self.address, "\n", self.email, self.phone)

