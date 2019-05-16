import tkinter as tk

from Particle import Particle
from Colour import Colour

class Display:
    def add(self,p):
        self._ps.append(p)

class TkDisplay(Display):

    def __init__(self):
        master = tk.Tk()
        w = tk.Canvas(master, width=600, height=400, bg='black')
        w.pack()
        self._p = Particle(30, (w.winfo_height() / 2, w.winfo_width() / 2), (80.0, 150.0), Colour(0,0,1))
        self._w = w
        self._fps = 60
        self._ps = []

    def draw_particle(self, p):
        r, x, y = p.r, p.x, p.y
        self._w.create_oval(x-r, y-r, x+r, y+r, outline="#"+p.colour.as_rgb_f())

    @property
    def bounding_box(self):
        return (0, self._w.winfo_width (),
                0, self._w.winfo_height())

    def update(self, dt):
        w,p = self._w, self._p
        w.delete(tk.ALL)
        for p in self._ps:
            p.move(dt)
            p.bounce(self.bounding_box)
            self.draw_particle(p)
        w.update()
        w.after(int(1000/self._fps), self.update, 1/self._fps)

    def go(self):
        self.update(0)
        tk.mainloop()

    def add(self,p):
        self.draw_particle
