from geometry.point import Point         # want to use both Point and Rectangle
from geometry.rectangle import Rectangle

def main():
    """  This is the starting point"""
    p = Point(3,2)
    r = Rectangle(p, 100, 200)
    print("The area is {0}".format(r.calculateArea()))

"""This if statement will only run with the main method when this script is given on the python command line"""
print(__name__)
if __name__ == "__main__":
    main()