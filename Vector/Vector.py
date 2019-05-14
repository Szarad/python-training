from math import sin,cos,pi,sqrt

class Vector:
   def  __init__(self, x, y):
        self.x = x
        self.y = y
   def __getitem__(self, n):
       if n==0:
           return self.x
       else:
           return self.y
   def __setitem__(self,n,v):
       if n==0:
           self.x = v
       else:
           self.y = v
       
   def  __add__(self,vector):
        return Vector(self.x + vector.x, vector.y + self.y)
   def  __sub__(self,vector):
        return Vector(self.x-vector.x, self.y-vector.y)
   def __mul__(self,s):
        return Vector(self.x*s, self.y*s)
   __rmul__ = __mul__
   def __truediv__(self,s):
        return Vector(self.x/s, self.y/s)
   
   def __neg__(self):
       return Vector(-self.x, -self.y)
   def __abs__(self):
       return sqrt(self.x*self.x + self.y*self.y)
  


