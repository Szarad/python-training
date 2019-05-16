import pyglet
from math import sin, cos, pi, sqrt
twopi = 2*pi

from Display  import Display

class PygletDisplay(Display):

    def __init__(self):
        self._w = pyglet.window.Window(600,400)
        self._fps_display = pyglet.clock.ClockDisplay()
        self._fps = 60
        self._ps = []
        self._w.event(self.on_draw)

    @property
    def bounding_box(self):
        return (0, self._w.width,
                0, self._w.height)

    def update(self, dt):
        for p in self._ps:
            p.move(dt)
            p.bounce(self.bounding_box)

    def on_draw(self):
        self._w.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield p.x + p.r * cos(angle)
                yield p.y + p.r * sin(angle)
                angle += delta_angle

        for p in self._ps:
            pyglet.gl.glColor3f(*p.c.as_rgb_01())
            pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                                 ('v2f', tuple(circle_vertices())))

        self._fps_display.draw()

    def go(self):
        pyglet.clock.schedule_interval(self.update, 1/self._fps)
        pyglet.app.run()

