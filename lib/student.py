#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name,  knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, string):
        self.string  = string
        return self.knowledge.append(self.string)
    
my_student = Student("My", "Student")
my_student.learn("New information")