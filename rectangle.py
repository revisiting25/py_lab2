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
        return self._height * 2 + self._width * 2
    
    def __eq__(self, value):
        if isinstance(value, Rectangle):
            return self.get_area() == value.get_area()
        else:
            return False
        
    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() <= other.get_area()
    
    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() < other.get_area()
    
    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() >= other.get_area()
    
    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_area() > other.get_area()
    

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height}, center: (x,y)=({self._x}, {self._y}))"

    def __str__(self):
        return f"Rectangle {self._width}x{self._height} (area={self.get_area()} and center at (x,y)=({self._x}, {self._y})"
