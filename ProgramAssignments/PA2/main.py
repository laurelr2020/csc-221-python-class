from geometry.point import Point         # want to use both Point and Rectangle
from geometry.rectangle import Rectangle

'''Write a main method in another module named main.py that instantiates several Shape objects, 
putting them in a list, then using a for loop to polymorphically call each object's calculateArea 
method and print each result.'''

def main():
    """  This is the starting point"""
    p = Point(3,2)
    r = Rectangle(p, 100, 200)
    print("The area is {0}".format(r.calculateArea()))

"""This if statement will only run with the main method when this script is given on the python command line"""
print(__name__)
if __name__ == "__main__":
    main()