from shape import Shape

class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init(x, y)

        self._radius = radius