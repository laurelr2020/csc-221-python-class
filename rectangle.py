from point import Point
class Rectangle:
    '''A Rectangle has an upper-left corner (type: Point), a width and a height'''
    def __init__(self, x, y, width, height):
        self.upperLeftCorner = Point(x,y)
        self.width = abs(width)
        self.height = abs(height)

    def calculateArea(self):
        '''This calculates the Area of the Rectangle'''
        return self.width * self.height