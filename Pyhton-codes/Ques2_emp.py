# create a class employee with attributes role, department, salary and showdetails as method

class Employee:
    def __init__(self,role ,salary, department):
        self.role = role
        self.salary = salary
        self.department = department
    
    def showempdetails(self):
         print(f"Your role is {self.role}\nYour department is {self.department}\nYour salary is {self.salary}")

# emp1 = Employee("Manager",100000,"Sales")
# emp2 = Employee("Marketing",90000,"Sales")
# emp1.showdetails()
# emp2.showdetails()


# create a class Engineer that inherits from Employee and add name and age attribute

class Engineer(Employee):
    def __init__(self, name, age, role, salary, department):
        super().__init__(role, salary, department)
        self.name = name
        self.age = age
    def showengdetail(self):
        print(f"Your name is {self.name}\nYour age is {self.age}")
        self.showempdetails()
     
eng1 = Engineer("Prabhat",20,"CEO",100000,"Head")
print(eng1.showengdetail())
