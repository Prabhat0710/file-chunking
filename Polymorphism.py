# Polymorphism in Python

# Polymorphism is the ability of different objects to respond to the same method or function in different ways.
# It allows for using a unified interface to work with objects of different types.

'''class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def display_number(self):
        print(self.real,"i +",self.img,"j")

c1 = Complex(9,6)
c1.display_number()
c2 = Complex(5,3)
c2.display_number()
'''

# But if i do this
# print(c1 + c2) #error

# mujhe apne class ke liye define krna h '+' ka matlab to add complex number

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def display_number(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num): # --> __add__ isko dunder function khte dunder yani double underscore iski help se ham apni definition de pay + ki
        real_part = self.real + num.real
        img_part = self.img + num.img
        return Complex(real_part, img_part)
    

c1 = Complex(9,6)
c1.display_number()
c2 = Complex(5,3)
c2.display_number()

addition = c1 + c2 # now i can add two imaginary numbers
addition.display_number() 

# Esi bhot sare DUNDER Function hote h jinka use krke ham operator ko kkhudki definiton de skte hai example __sub__ , __truediv__