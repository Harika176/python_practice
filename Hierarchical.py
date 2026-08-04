class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display_info(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
class Car(Vehicle):
    def display_info(self):
        print("Car Brand:",self.brand)
        print("Maximum Speed:",self.speed,"km/h")
class Bike(Vehicle):
    def display_info(self):
        print("Bike Brand:",self.brand)
        print("Maximum Speed:",self.speed,"km/h")
car=Car("Toyota",180)
bike=Bike("Yamaha",120)
car.display_info()
bike.display_info()