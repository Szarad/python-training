import tkinter as tk
from  Particle import Particle
from math import sin,cos,pi,sqrt


class TkinterDisplay:
    def __init__(self):
        master = tk.Tk()
        self._w = tk.Canvas(master, width=600, height=400, bg='black')
        self._w.pack()
        self._p = Particle(30,(self._w.winfo_height() / 2, self._w.winfo_width() / 2), (80.0,150.0))
    def bounding_box(self):
        return 0,self._w.winfo_width() , 0, self._w.winfo_height()

    def draw_particle(self,p):
        r,x,y = self._p.r, self._p.x, self._p.y
        self._w.create_oval()
    def update(self,dt):
        self._w.delete(tk.ALL)
        self._p.move(dt)
        self._p.bounce(self.bounding_box())
        self.draw_particle(self._p)
        self.update()
        self._w.after(int(1000/60), 1/60)

    def go(self):
        self.update(0)
        tk.mainloop
         

