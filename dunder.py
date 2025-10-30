# Qs. Create a class called Order which stores item & its price.Use Dunder function __gt__ ) to convey that:
# orderl > order2 if price of orderl > price of order2

# class Order:
#     def __init__(self, item, prize):
#         self.item = item
#         self.prize = prize

#     def __gt__(self, product):
#         return self.prize > product.prize

# pro1 = Order("Smartphone",20)
# pro2 = Order("Notebook",100)

# print(pro1 > pro2)



# manipulate global variable inside class
# use constructor to keep count no of object of a class
# use desdructor to decrease the no of object when the object of a class is deleted
# method and function difference

a = "hi"
count_object = 0
delete_object = 0
class Car:    
    __color = "Black"
    __engine_power = 1000   

    def __init__(self):
        global count_object
        count_object += 1
    
    def __del__(self):
        global count_object
        global delete_object
        count_object -= 1
        delete_object += 1

    def get_value(self):
        return (f"{self.__color} and {self.__engine_power}")
    
    def set_colorvalue(self,new_color):
        global a
        a = "hello"
        if new_color == "":
            print("Enter a valid color")
            return        
        self.__color = new_color
    
    def set_enginevalue(self,new_enginepower):
        self.__engine_power = new_enginepower
    
    def fetch(self,another_carobject):
        print(another_carobject.get_value())

    def spec(self):
        print("This car is of color",self.__color,"and has a power of",self.__engine_power,a)  # a is accesible in class Car because its a global variable {LEGB method --> Local Enclosing Global Built in}
    
    def get_object_count(self):
        global count_object
        return count_object
    
    def get_deleted_objectcount(self):
        global delete_object
        return delete_object


c1 = Car()
# c1.set_colorvalue("White")
# c1.spec()
c2 = Car()
c3 = Car()
print(count_object) # 3
del c1
print(delete_object) # 1
print(count_object) # 2
