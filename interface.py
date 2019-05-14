#!/usr/bin/python

import sys
import subprocess
import pyglet
import tkinter as tk
from  Particle import Particle
from math import sin,cos,pi,sqrt
if sys.argv[1] == 'tk':
        
        master = tk.Tk()
        def draw_particle(canvas,p):
            r,x,y = p.r, p.x, p.y
            canvas.create_oval(x-r, y-r, x+r, y+r, outline='yellow')
        
        w = tk.Canvas(master, width=600, height=400, bg='black')
        w.pack()
        p = Particle(30,(w.winfo_height() / 2, w.winfo_width() / 2), (80.0,150.0))
        xmin=0
        ymin=0
        fps=60
        draw_particle(w,p)
        def update(dt):
                w.delete(tk.ALL)
                p.move(dt)            
                p.bounce((0, w.winfo_width(),0,w.winfo_height()))
                draw_particle(w,p)
                w.update()
                w.after(int(1000/fps), update, 1/fps)
        update(0)

        tk.mainloop()
elif sys.argv[1] == 'pyglet':

        twopi = 2*pi 
       # print(type(pyglet.window))
       # window = pyglet.window.Window(10,10)
        
        w = pyglet.window.Window(600,400)
        fps_display = pyglet.clock.ClockDisplay()
        p = Particle(30,(w.width / 2, w.height / 2), (80.0,150.0))
        
        xmin=0
        ymin=0
        fps=60


        @w.event
        def on_draw():
            w.clear()
            def circle_vertices():
                delta_angle = twopi / 20
                angle = 0
                while angle < twopi:
                    yield p.x + p.r * cos(angle)
                    yield p.y + p.r * sin(angle)
                    angle += delta_angle
            pyglet.gl.glColor3f(1.0, 1.0, 0)
            pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

        fps_display.draw()


        def update(dt):
            p.move(dt)
            p.bounce((0, w.width, 0, w.height))

        pyglet.clock.schedule_interval(update, 1/60.0)
        pyglet.app.run()
