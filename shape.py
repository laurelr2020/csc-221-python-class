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
