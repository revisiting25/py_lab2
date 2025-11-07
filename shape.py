class Shape:
    def __init__(self, x = 0, y = 0):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("Center x and y must be numerical values (int or float).")

        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    def translate(self, dx, dy):
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("Translation dx and dy must be numerical values (int or float).")
        self._x += dx
        self._y += dy