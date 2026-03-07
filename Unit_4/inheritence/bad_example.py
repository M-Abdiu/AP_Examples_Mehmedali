class Rectangle:
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h


class Square(Rectangle):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w
        self._height = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._width = h
        self._height = h


def resize(rect: Rectangle):
    rect.width = 5
    rect.height = 4
