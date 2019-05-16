from Colour import Colour

class Model:
    def __init__(self, Colour, shape):
        self.col = Colour
        self.shape = shape
        w = tk.Canvas(master, width=600, height=400, bg='black')
        self._w = w

    def draw(self, ob):
        r,x,y = ob.r, ob.x,ob.y
        self._w.create+"_"+self.shape(x-r, y-r, x+r, y+r, outline="#"+self.col.as_rgb_f())
    def update(self, dt):
        w = self._w
        w.delete(tk.ALL)
              
        
   


