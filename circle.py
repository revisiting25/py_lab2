from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numerical value (int or float).")
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")

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
        
    def __le__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius <= other._radius
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius
    
    def __ge__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius >= other._radius
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius
    

    def __repr__(self):
        return f"Circle(radius={self._radius}, center: (x,y)=({self._x}, {self._y}))"

    def __str__(self):
        return f"Circle with radius {self._radius} and center at (x,y)=({self._x}, {self._y})"