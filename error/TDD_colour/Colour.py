class Colour:

    def __init__(self, r,g,b):
        self._rgb_01 = (r,g,b)

    @classmethod
    def from_rgb_01(cls, r,g,b):
        return cls(r,g,b)

    def as_rgb_01(self):
        return self._rgb_01

    f_to_n = {d:n for n,d in enumerate('0123456789abcdef')}
    n_to_f = {n:d for d,n in f_to_n.items()}

    def as_rgb_f(self):
        return ''.join(self.n_to_f[int(v*15)] for v in self._rgb_01)

    @staticmethod
    def from_rgb_f(rgb):
        c = Colour(*(Colour.f_to_n[d] / 15.0 for d in rgb.lower()))
        return c

    def __hash__(self):
        return hash(self._rgb_01)
    def __eq__(self, col):
        return self._rgb_01 == col._rgb_01
        
Color = Colour
'''
colour_k=[Colour.BLACK, Colour.WHITE, Colour.RED, Colour.GREEN, Colour.BLUE,Colour.YELLOW, Colour.CYAN, Colour.MAGNETA]
colour_v=[Colour.from_rgb_01(0,0,0), Colour.from_rgb_01(1,1,1), Colour.from_rgb_01(1,0,0), Colour.from_rgb_01(0,1,0), Colour.from_rgb_01(0,0,1), Colour.from_rgb_01(1,1,0), Colour.from_rgb_01(0,1,1),Colour.from_rgb_01(1,0,1) ]
Colour_dict = dict(zip(colour_k,colour_v))

print(Colour_dict['BLACK'])
'''
c = Colour()
Colour.BLACK   = Colour.from_rgb_01(0,0,0)
Colour.WHITE   = Colour.from_rgb_01(1,1,1)
Colour.RED     = Colour.from_rgb_01(1,0,0)
Colour.GREEN   = Colour.from_rgb_01(0,1,0)
Colour.BLUE    = Colour.from_rgb_01(0,0,1)
Colour.YELLOW  = Colour.from_rgb_01(1,1,0)
Colour.CYAN    = Colour.from_rgb_01(0,1,1)
Colour.MAGENTA = Colour.from_rgb_01(1,0,1)


