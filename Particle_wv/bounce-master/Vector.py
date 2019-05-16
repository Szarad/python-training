from math import sqrt

class Vector:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __getitem__(self, n):
        if n == 0: return self.x
        if n == 1: return self.y
        raise IndexError

    def __setitem__(self, n, v):
        if   n == 0: self.x = v
        elif n == 1: self.y = v
        else: raise IndexError

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Vector(self.x / scalar,
                      self.y / scalar)

    def __abs__(self):
        x,y = self
        return sqrt(x*x + y*y)
