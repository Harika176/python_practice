from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=1
        self.w=w
    def area(self):
        return self.l*self.w
shapes=[Circle(5),Rectangle(4,6)]
for shape in shapes:
    print(shape.area())