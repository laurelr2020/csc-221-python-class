from shape import Rectangle
from shape import Square


class RectangleSquare(Rectangle, Square):
    def __init__(self):
        print("Initializing a RectangleSquare")