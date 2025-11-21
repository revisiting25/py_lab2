from shape import Shape
from functools import total_ordering 
import math

@total_ordering
class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        super().__init(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numerical value (int or float).")
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")

        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return math.pi * (self._radius ** 2)
    
    @property
    def perimeter(self):
        return math.pi * self._radius * 2
    

    def is_unit_circle(self):
        """Check if the circle is the unit circle and return True if radius = 1 and center at (x,y)=(0,0)"""
        return (
            math.isclose(self._radius, 1.0) and
            math.isclose(self._x, 0.0) and
            math.isclose(self._y, 0.0)
        )
    
    # Operator overrides
    def __eq__(self, other):
        return isinstance(other, Circle) and math.isclose(self._radius, other._radius)
        
    # Thanks to @total_ordering, we only need to define __lt__ and __eq__
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius
    
    ## The following comparison methods are not needed due to @total_ordering
    # def __le__(self, other):
    #     if not isinstance(other, Circle):
    #         return NotImplemented
    #     return self._radius <= other._radius
    
    # def __ge__(self, other):
    #     if not isinstance(other, Circle):
    #         return NotImplemented
    #     return self._radius >= other._radius
    
    # def __gt__(self, other):
    #     if not isinstance(other, Circle):
    #         return NotImplemented
    #     return self._radius > other._radius
    

    def __repr__(self):
        return f"Circle(radius={self._radius}, center: (x,y)=({self._x}, {self._y}))"

    def __str__(self):
        return f"Circle with radius {self._radius} and center at (x,y)=({self._x}, {self._y})"