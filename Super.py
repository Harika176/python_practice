class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def display_info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
car=Car("Toyota","Innova")
car.display_info()