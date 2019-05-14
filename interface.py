#!/usr/bin/python

import sys
import subprocess
import pyglet
import tkinter as tk
import Particle

if sys.argv[1] == 'tk':
        master = tk.Tk()
        w = tk.Canvas(master, width=600, height=400, bg='black')
        w.pack()
       # x,y = w.winfo_height() / 2, w.winfo_width() / 2
        #vx, vy = 80.0, 150.0
		r=60
		
		p = Particle(r,(w.winfo_height() / 2, w.winfo_width() / 2), (80.0,150.0))
        particle = w.create_oval(x,y, 60,60, outline='yellow')
        def update(dt):
				w.delete(tk.ALL)
				p.move(dt)			
				p.bounce((0, w.winfo_width(),0,w.info_height()))
				draw_particle(w,p)
				w.update()
				w.after(int(100/fps), update, 1/fps)
        update(0)

        tk.mainloop()




else:
        radius = 30
        constant_angel = 20
        position_x = 30
        position_y = 30
        window = pyglet.window.Window(600,400)
        fps_display = pyglet.clock.ClockDisplay()

        x,y = window.width / 2, window.height / 2
        vx, vy = 80.0, 150.0

        @window.event
        def on_draw():
                window.clear()
        def circle_vertices():
                delta_angle = twopi / constant_angel
                angle = 0
                while angle < twopi:
                                yield x + radius * cos(angle)
                                yield y + radius * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                         ('v2f', tuple(circle_vertices())))

        fps_display.draw()


        def update(dt):
                #global x,y, vx, vy
                x += vx*dt
                y += vy*dt

                if x + radius > window.width:
                        x = window.width - radius
                        vx = - vx

                if x - radius < 0:
                        x =  radius
                        vx = - vx

                if y + radius > window.height:
                        y = window.height - radius
                        vy = - vy


                if y - radius < 0:
                        y = radius
                        vy = - vy

        pyglet.clock.schedule_interval(update, 1/60.0)

        pyglet.app.run()
