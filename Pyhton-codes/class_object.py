# CLass :- its a blueprint for creating objects (example: car banane ke liye bluprint tyar krte h)
# Object :- its a instance of class (car ko bnane ke liye bluprint to bna dia ab car b to bnani hogi vo car object h)


# Ques1 :- create a class that takes name and marks of a student in 3 subject in constructor and calculate avg in method.
class Student:
    # constructor
    def __init__(self, name, maths, science, english):
        self.name = name  # instance variable or attribute
        self.maths = maths
        self.science = science
        self.english = english

    def avgerage(self):
        total = self.maths + self.science + self.english
        avg = total / 3
        print(f"Name: {self.name}, Average Marks: {avg}")


s1 = Student("prabhat", 85, 90, 95)
s1.avgerage()

s1.name = "Prabhat Singh"  # changing the name attribute
s1.avgerage() 