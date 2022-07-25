#!/bin/python3

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) # get values from Person class
        self.scores = scores

    def calculate(self):
        res = 0
        for i in scores:
            res += i
        res = res / len(scores)
        if res >= 90:
            return 'O'
        elif res >= 80 and res < 90:
            return 'E'
        elif res >= 70 and res < 80:
            return "A"
        elif res >= 55 and res < 70:
            return 'P'
        elif res >= 40 and res < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) 
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())