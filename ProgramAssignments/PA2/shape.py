import math
import abc

'''Finish the Python module named shape.py by adding definitions for Ellipse and Circle, 
which should be related to Shape in the same way that Rectangle and Square are. '''

class Shape:
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def calculateArea(self):
        pass

    @abc.abstractclassmethod
    def getShape(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def  calculateArea(self):
        return self.width * self.height

    def getShape(self):
        return "Rectangle"

class Square(Rectangle): 
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)

    def getShape(self):
        return "Square"

class Ellipse(Shape):
    def __init__(self, horizontalRadius, verticalRadius):
        self.horizontalRadius = abs(horizontalRadius)
        self.verticalRadius = abs(verticalRadius)

    def calculateArea(self):
        return (math.pi * self.horizontalRadius * self.verticalRadius)

    def getShape(self):
        return "Ellipse"

class Oval(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def getShape(self):
        return "Oval"
