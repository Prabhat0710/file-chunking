# Inheritance :- inheritance is a mechanism in which one class can inherit the properties and methods of another class.

class Car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")

class Tata(Car):
    def __init__(self, model_name):
        self.model_name = model_name

    def display_model(self):
        print("Model Name : ",self.model_name)


c1 = Tata("Harrier")
print(c1.start())
print(c1.stop())
print(c1.display_model())