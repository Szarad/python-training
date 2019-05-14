class Particle:

	def __init__(self,r, x,y, vx,vy):
		self.vx = vx
		self.vy = vy
		self.r = r
		self.x = x
		self.y = y

	def move(self,dt):
		
		self.x += self.vx*dt 
		self.y += self.vy*dt
		
	def bounce(self):
		if self.x + self.r > window.width:
			self.x = window.width - self.r
			self.vx = - self.vx

		if self.x - self.r < 0:
			self.x =  self.r
			self.vx = - self.vx

		if self.y + self.r > window.height:
			self.y = window.height - self.radius
			self.vy = - self.vy

		if self.y - self.r < 0:
			self.y = self.r
			self.vy = - self.vy

		 
		
