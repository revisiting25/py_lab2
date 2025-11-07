class Shape:
    def __init__(self, x = 0, y = 0):

        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    def translate(self, dx, dy):
        self._x += dx
        self._y += dy