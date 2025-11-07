import math
from shape import Shape

class Rectangle(Shape):
    def __init__(self, x = 0, y = 0, width = 1, height = 1):
        super().__init__(x, y)

        self._width = width
        self._height = height

    def get_area(self):
        return self._height * self._width
    
    def get_perimeter(self):
        return math.sqrt(self._height ** 2 + self._width ** 2)
    
    def __eq__(self, value):
        if isinstance(value, Rectangle):
            return self.get_area() == value.get_area()
        else:
            return False