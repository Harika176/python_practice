class Shape:
    def __init__(self,color):
        self.color=color
class Circle(Shape):
    def __init__(self, color,radius):
        super().__init__(color)
        self.radius=radius
    def display_info(self):
        print("Color:",self.color)
        print("Radius:",self.radius)
class Rectangle(Shape):
    def __init__(self, color,length,width):
        super().__init__(color)
        self.length=length
        self.width=width
    def display_info(self):
        print("Color:",self.color)
        print("Length:",self.length)
        print("Width:",self.width)
circle=Circle("Red",7)
rectangle=Rectangle("Pink",8,3)
circle.display_info()
rectangle.display_info()