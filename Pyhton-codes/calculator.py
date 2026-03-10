# Create a calculator class with methods for all operation and also sanitize(if divide by 0 is given, give error) the input
# Create a method for calculating (a + b)^2 value 
# Create a method to calculate gravitational pull {F = (G*M*m)/R^2} bwt two masses
 
class Calculator:
    def add(self,num1,num2):
        return num1 + num2 
    
    def subtract(self, num1,num2):
        if num1 > num2:
            return num1 - num2
        else:
            return num2 - num1
        
    def division(self, num1,num2):
        if num2 != 0:
            return num1/num2
        else:
            return "Error, Can't divide by zero"
    
    def multiply(self, num1,num2):
        return num1 * num2
    
    def square(self, num1, num2):
        sq_sum = num1 + num2
        return self.multiply(sq_sum,sq_sum)
    
    def gravitation_pull(self,m1,m2,r):
        G = 6.6 * 10**(-11)
        F = (G * m1 * m2) / r**2
        return F

cal = Calculator()

print("---My Calculator---")
while True:
    print("[ 1 = sum, 2 = sub , 3 = multiply, 4 = division, 5 = (a + b)^2, ], 6 = gravitational pull")
    ask = int(input("What operation do you want to do (1,2,3,4,5)\n"))
    if ask in [1,2,3,4,5]:
        num1 = int(input("Enter first number\n"))
        num2 = int(input("Enter second Number\n"))
        if ask == 1:
            print(cal.add(num1,num2))
        elif ask == 2:
            print(cal.subtract(num1, num2))
        elif ask == 3:
            print(cal.multiply(num1,num2))
        elif ask == 4:
            print(cal.division(num1, num2))
        elif ask == 5:
            print(cal.square(num1,num2))
    elif ask == 6:
        mass1 = int(input("Enter mass of 1st object\n"))
        mass2 = int(input("Enter mass of 2nd object\n"))
        radius = int(input("Enter radius\n"))
        print(cal.gravitation_pull(mass1,mass2,radius))
    else:
        print("Enter valid input [ 1 = sum, 2 = sub , 3 = multiply, 4 = division, 5 = (a + b)^2, ], 6 = gravitational pull")
    
    cont = input("Enter 'Y' if you want to continue, 'N' to stop\n").capitalize()
    if cont == 'N':
        break