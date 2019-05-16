import tkinter as tk

from Display  import Display

class TkDisplay(Display):

    def __init__(self):
        master = tk.Tk()
        w = tk.Canvas(master, width=600, height=400, bg='black')
        w.pack()
        self._ps = []
        self._w = w
        self._fps = 60

    def draw_particle(self, p):
        r, x, y = p.r, p.x, p.y
        self._w.create_oval(x-r, y-r, x+r, y+r, outline="#"+p.c.as_rgb_f())

   # def draw_square(self,p):


    @property
    def bounding_box(self):
        return (0, self._w.winfo_width (),
                0, self._w.winfo_height())

    def update(self, dt):
        w = self._w
        w.delete(tk.ALL)
        for p in self._ps:
            
            '''
            p.move(dt)
            p.bounce(self.bounding_box)
            self.draw_particle(p)
            '''

        w.update()
        w.after(int(1000/self._fps), self.update, 1/self._fps)

    def go(self):
        self.update(0)
        tk.mainloop()

