import abc

class Shape(metaclass=abc.ABCMeta):

    numberOfShapes = 0

    def __init__(self):
        Shape.numberOfShapes += 1

    @abc.abstractmethod
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
        super().__init__()
        if width < 0:
            width = 0
        if height < 0:
            height = 0
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)