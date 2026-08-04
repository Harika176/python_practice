class Vehicle:
    def display_info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def display_info(self):
        print("This is a car")
class Bike(Vehicle):
    def display_info(self):
        print("This is a bike")
v=Vehicle()
c=Car()
b=Bike()
v.display_info()
c.display_info()
b.display_info()