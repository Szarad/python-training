class Colour:
    
    @staticmethod
    def from_rgb_01(r,g,b):
        c = Colour()
        c.rgb = (r,g,b)
        return c
        
    def as_rgb_01(self):
        return self.rgb

    @classmethod
    def as_rgb_f(c):
        c = Colour()
        return c.rgb


Colour.BLACK = Colour.from_rgb_01(0,0,0)
Colour.WHITE = Colour.from_rgb_01(1,1,1)
Colour.RED = Colour.from_rgb_01(1,0,0)
Colour.GREEN = Colour.from_rgb_01(0,1,0)
Colour.BLUE = Colour.from_rgb_01(0,0,1)
Colour.YELLOW = Colour.from_rgb_01(1,1,0)
Colour.CYAN = Colour.from_rgb_01(0,1,1)
Colour.MAGENTA = Colour.from_rgb_01(1,0,1)


Color=Colour
