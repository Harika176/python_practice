class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def __str__(self):
        return f"Car(Brand:{self.brand},Model:{self.model})"
c=Car("BMW","Innova")
print(c)