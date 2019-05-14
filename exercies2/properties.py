class Rectangle:
	def __init__(self,w,h):
		self.w = w
		self.h = h
		self.a = w * h
	@property	
	def a(self):
		return self.w * self.h
	@a.setter #(make suer setter and getter have the same name)
	def a(self, new_a):
		self.w = new_a / self.h

r = Rectangle(2,3)
assert r.w == 2
assert r.h == 3
# without @property
#assert r.a() == 6
assert r.a == 6
r.w = 4

r.a = 6

assert r.w == 2
assert r.h == 3
#without @property
#assert r.a() == 12
#with property
assert r.a == 6

print("ok")

