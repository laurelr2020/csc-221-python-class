from thirddimension import ThirdDimension
from shape import Square

class Cube(Square, ThirdDimension):
    def __init__(self, side):
        print("Init Cube")
        Square.__init__(self, side)
        self.depth = side  #avoids calling constructor for object twice.