import pyglet
from math import sin,cos,pi,sqrt
from  Particle import Particle

twopi = 2*pi
class PygletDisplay:
    def __init__(self):
        self._w = pyglet.window.Window(600, 400)
        self._w.event(self.on_draw)
        self._fps_display = pyglet.clock.ClockDisplay()
        self._fps=60
        self._p = Particle(30, (self._w.width/2, self._w.height / 2), (80.0, 150.0))
    
    def bounding_box(self):
        return 0, self._w.width,0, self._w.height
   # @window.events 
    def on_draw(self):
        self._w.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield self._p.x + self._p.r*cos(angle)
                yield self._p.y + self._p.r*sin(angle)
                angle +=delta_angle
        pyglet.gl.glColor3f(1.0, 1.0, 0)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                   ('v2f', tuple(circle_vertices())))
        self._fps_display.draw()

    def update(self,dt):
         self._p.move(dt)
         self._p.bounce(self.bounding_box())
    def go(self):
         pyglet.clock.schedule_interval(self.update, 1/60.0)
         pyglet.app.run()
