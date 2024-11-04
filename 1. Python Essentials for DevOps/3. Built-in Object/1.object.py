'''
In OOP, data or state and functionality appear together. The essential concepts to understand when working with objects are class 
instantiation (creating objects from classes) and dot syntax (the syntax for accessing an object’s attributes and methods). 
A class defines attributes and methods shared by its objects. Think of it as the techni‐ cal drawing of a car model. The class can 
then be instantiated to create an instance. The instance, or object, is a single car built based on those drawings.
'''

class FancyCar():
    pass
print(type(FancyCar))

my_car = FancyCar()
print(type(my_car))

'''
These functions have access to the object’s attributes and can modify and use the object’s data. To call an object’s method or access 
one of its attributes, we use dot syntax:
'''

class FancyCar():
    wheels = 4
    def driveFast(self):
        print("Driving so fast")

my_car = FancyCar()
print(my_car.wheels)

my_car.driveFast()
    
