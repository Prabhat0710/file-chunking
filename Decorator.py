# static method :- bina self parameter ke use krwa skte hai

'''class Car:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def status():
        print("Your car is ready")

c1 = Car("Prabhat")
print(c1.name)
c1.status()
'''

# class method :- class attribute ko access krne ke liye use krte hai

'''
class Person:
    name = "Anonymouse" #class attribute 
    def changename(self, name):
        self.name = name


p1 = Person()
p1.changename("Person") # it gives value "person" to (changename :- name)
print(p1.name)
print(Person.name) # different ouput

# example
class Person:
    name = "Anonymouse" #class attribute 
    @classmethod
    def changename(cls, name):
        cls.name = name


p1 = Person()
p1.changename("Person") #now it gave value "person" to class attribute i.e name 
print(p1.name)
print(Person.name) # now same output as p1.name
'''

# property :- ese attribute jinki value fix na rkhni ho aur changing variable ke sath change hoti rhe

class Marks:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percent = (self.phy + self.chem + self.maths)/3

m1 = Marks(98,99,97)
print(m1.percent)
m1.maths = 86
print(m1.percent) #same output even after changing marks of maths

# solution
class Marks:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    @property
    def percent(self):
        return (self.phy + self.chem + self.maths)/3

m1 = Marks(98,99,97)
print(m1.percent)
m1.maths = 86
print(m1.percent) # now the output is changed according to new data feeded