from Vector import Vector

class Particle:

    def __init__(self, r, pos, velo):
        position = Vector(pos[0], pos[1])
        velocity = Vector(velo[0], velo[1])
        #self.vx = velo[0]
        #self.vy = velo[1]
        self.r = r
       # self.x = pos[0]
       # self.y = pos[1]

    def move(self, dt):
        position += dt
        #self.x += self.vx*dt
        #self.y += self.vy*dt

    def bounce(self, minmax):
        x_min, x_max, y_min, y_max = minmax

        if self.x + self.r > x_max:
            extra = x_max - (self.x + self.r)
            self.x += 2*extra
            self.vx = - self.vx

        if self.x - self.r < x_min:
            extra = x_min - (self.x - self.r)
            self.x += 2*extra
            self.vx = - self.vx

        if self.y + self.r > y_max:
            extra = y_max - (self.y + self.r)
            self.y += 2*extra
            self.vy = - self.vy

        if self.y - self.r < y_min:
            extra = y_min - (self.y - self.r)
            self.y += 2*extra
            self.vy = - self.vy
