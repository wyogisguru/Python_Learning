#-------------------------------------------------------------------------------
# Name:        Class Object: 'Student'
# Purpose:
#
# Author:      cbrink
#
# Created:     07/01/2016
# Copyright:   (c) cbrink 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Student:
    """
    A class object that figures student grades.

    """
    def __init__(self, name, _class):
        self.name = name
        self._class = _class
        self.grades = []

    def letter_grade(self, test_score):
        if (test_score >= 90 and test_score <= 100):
            self.grades.append('A')
            print(self.name + ' is a ' + self._class + ' and got a A!')
        elif (test_score >= 80 and test_score <= 89):
            self.grades.append('B')
            print(self.name + ' is a ' + self._class + ' and got a B!')
        elif (test_score >= 70 and test_score <= 79):
            self.grades.append('C')
            print(self.name + ' is a ' + self._class + ' and got a C!')
        elif (test_score >= 60 and test_score <= 69):
            self.grades.append('D')
            print(self.name + ' is a ' + self._class + ' and got a D!')
        else:
            self.grades.append('F')
            print(self.name + ' is a ' + self._class + ' and got a F!')

def main():
    student1 = Student('Chris', 'Junior')
    student1.letter_grade(88)
    student1.letter_grade(74)
    student1.letter_grade(93)
    student1.letter_grade(100)
    print(student1.grades)

if __name__ == '__main__':
    main()
