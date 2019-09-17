import math
class Shape:
    def __init__(self):
        pass

    def calculateArea(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def  calculateArea(self):
        return self.width * self.height

class Square(Rectangle): 
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)

class Ellipse(Shape):
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def calculateArea(self):
        return (math.pi * self.width * self.height)

class Oval(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
