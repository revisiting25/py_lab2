from shape import Shape

class Rectangle(Shape):
    def __init__(self, x = 0, y = 0, width = 1, height = 1):
        super().__init__(x, y)

        self._width = width
        self._height = height