class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, weith, higth):
        self.higth = higth
        self.weith = weith
        super().__init__()

    def area(self):
        return self.weith * self.higth
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
    def area(self):
        from math import pi
        return (self.radius**2)*pi
    
square = Square(3,4)
circle = Circle(4)

print(square.area())
print(circle.area())
