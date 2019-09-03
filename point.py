class Point:
    """Point is a representation of a two dimensional point as in analytic geometry. There are two attributes, x and y."""

    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        
    def reset(self):
        self.x = 0
        self.y = 0

