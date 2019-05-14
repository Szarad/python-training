class Vector2D:
    __init__(self, x, y):
        self.x = x
        self.y = y
    __add__(self,x1,y1,x2,y2):
        return Vector(self.x1 + self.x2, self.y1 + self.y2)
    __substraction__(self,x1,y1,x2,y2):
        return Vector(self.x1-self.x2, self.y1-self.y2)

