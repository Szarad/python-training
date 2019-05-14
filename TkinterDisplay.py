class TkinterDisplay:
    def __init__(self):
        master = tk.Tk()
        self._w = tk.Canvas(master, width=600, height=400, bg='black')
        self._w.pack()
        self.p = Particle(30,(w.winfo_height() / 2, w.winfo_width() / 2), (80.0,150.0))

    def update(self,dt):
        w.delete(tk.ALL)
        p.move(dt)
         

