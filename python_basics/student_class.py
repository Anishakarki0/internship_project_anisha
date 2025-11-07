#-Student class with name, age, marks, and grade calculation
#
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

student1 = Student("Anisha", 20, 85)
print(f"{student1.name}'s grade is {student1.get_grade()}")
