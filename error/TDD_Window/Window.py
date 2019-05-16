class Window:
   # @staticmethod #without need of instance
    @classmethod
    def from_corners(cls,lo,hi):
        xl,yl = lo
        xh, yh = hi
        #x = (xl + xh) / 2
        #y  = (yl + yh) /2
        width = xh - xl
        height = yh - yl
        return cls((xl, yl),(width,height))
    def __init__(self, corner, size):
        xlo, ylo =corner
        dx,dy = size
        self._x = xlo + dx/2
        self._y = ylo + dy/2
        self.width, self.height = size
    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @y.setter
    def y(self, _):
        raise AttributeError
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
#BorderWindow = Window
class BorderWindow(Window):
    def __init__(self, corner, size):
        x,y = corner
        w,h = size
        Window.__init__(self, (x-5,y-5), (w+10,h+10))
        '''xlo, ylo =corner
        dx,dy = size
        self._x = xlo + dx/2
        self._y = ylo + dy/2
        self.width, self.height = size'''
    #def area(self):
    #    return (self.width+10) * (self.height+10)


