'''Write a main method in another module named main.py that instantiates several Shape objects, 
putting them in a list, then using a for loop to polymorphically call each object's calculateArea 
method and print each result.'''

from shape import Shape, Rectangle, Ellipse, Square, Oval

def main(self):
    square = Square(5)
    rectangle = Rectangle(12,5)
    ellipse = Ellipse(4, 10)
    oval = Oval(-4)

    shapeList = [square, rectangle, ellipse, oval]

    for s in shapeList:
        if isinstance(s, Shape):
            print("This " + s.getShape() + " has an area of " + s.calculateArea())