import pyglet
from math import sin, cos, pi, sqrt
twopi = 2*pi

from Particle import Particle
from Colour import Colour
class PygletDisplay:

    def __init__(self):
        self._w = pyglet.window.Window(600,400)
        self._fps_display = pyglet.clock.ClockDisplay()
        self._fps = 60
        self._p = Particle(30, (self._w.width / 2, self._w.height / 2), (80.0, 150.0), Colour(1,0,0))
        p = self._p
        print(p.colour)
        self._w.event(self.on_draw)

    @property
    def bounding_box(self):
        return (0, self._w.width,
                0, self._w.height)

    def update(self, dt):
        self._p.move(dt)
        self._p.bounce(self.bounding_box)

    def on_draw(self):
        self._w.clear()
        p = self._p
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(*p.colour.as_rgb_01())
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        self._fps_display.draw()

    def go(self):
        pyglet.clock.schedule_interval(self.update, 1/self._fps)
        pyglet.app.run()

    def add(self, p):
        p.on_draw()
        p.update()
