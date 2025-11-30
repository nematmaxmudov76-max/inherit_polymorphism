class Shape:
    def __init__(self):
        pass
    def area(self):
        print("maydon yuzi..")
class Rectangle(Shape):
    def __init__(self, boyi, eni):
        self.boyi = boyi
        self.eni = eni
        super().__init__()
    def __str__(self):
        print(f"yuzasi:{self.boyi * self.eni}")
        return super().__str__()
rec = Rectangle(
    boyi = 4,
    eni = 3
)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
    def __str__(self):
        from math import pi
        print(f"aylana yuzi:{(self.radius**2)*pi}")
        return super().__str__()
    
cir = Circle(
    radius=2
)

print(rec.__class__.__name__)  #o'ziga nima yuklangan shuni chop etadi
print(cir.__class__.__name__)  #o'ziga nima yuklangan shuni chop etadi