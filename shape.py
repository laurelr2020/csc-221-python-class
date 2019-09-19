import abc
class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    
    @abc.abstractclassmethod
    def calculateArea(self):
        pass

class ShapeList(list):
    def append(self, newMember):
        if isinstance(newMember, Shape):
            super().append(newMember)

    def printAreas(self):
        for s in self:
            if isinstance(s, Shape):
                print(s.calculateArea())

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def  calculateArea(self):
        return self.width * self.height

class Square(Rectangle): 
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)