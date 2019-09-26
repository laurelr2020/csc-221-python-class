import abc 

class ThirdDimension(metaclass=abc.ABCMeta):
    def __init__(self, depth):
        self.depth = abs(depth)

    def calculateVolume(self):
        return self.calculateArea() * self.depth

    @abc.abstractclassmethod
    def calculateArea(self):
        pass