from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init(x, y)

        self._radius = radius

    def get_radius(self):
        return self._radius
    
    def get_area(self):
        return math.pi * (self._radius ** 2)
    
    def get_perimeter(self):
        return math.pi * self._radius * 2
    
    def __eq__(self, value):
        if isinstance(value, Circle):
            return self._radius == value._radius
        else:
            return False