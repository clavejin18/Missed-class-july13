#!/usr/bin/python3

class Roster:
    
    # required definitions
    def rosterInfo(self):
        self.students = []

    def add(self, student):
        self.students.append(student)
    
    def summarize(self):
        for student in self.students:
           print('Contact information for {0}. {1} is:'.format(student.first_name[0], student.last_name))
           student.printInfo()
        