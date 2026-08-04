from abc import ABC,abstractmethod
class Shape:
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
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
Shapes=[
Circle(5),
Rectangle(4,6)
]
for Shape in Shapes:
    print(Shape.area())
