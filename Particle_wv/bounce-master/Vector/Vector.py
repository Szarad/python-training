from operator import add, sub


def Vector(bindings):
    class The_Class(object):
        def __init__(self, *dim):
            self._d = list(dim)
        def __getitem__(self,n):
            return self._d[n]
        def __setitem__(self,n,v):
            self._d[n]=v
        def __add__(self,other):
            return Vector(list( map(add, self._d, other._d)))
        def __sub__(self,other):
            return Vector((x1 - x2 for x1,x2 in zip(self._d, other._d)))
        def __neg__(self):
            return Vector(-1*x for x in self._d)
        def __mul__(self, s):
            return Vector(x*s for x in self._d)
        __rmul__ = __mul__
        def __truediv__(self,s):
            return Vector(x/s for x in self._d)
        def __abs__(self):
            return Vector(x*x for x in self_d)
                
        def separate_binding_of_i(i):
            def closure():
                return i
            return closure
        
        def fresh_binding_of_d(self):
            closure = separate_binding_of_i(i)
            return self._d(closure)
        

       for  i, name in enumerate(bindings):
           setattr(The_Class, name, property(lambda self:self.fresh_binding_of_d())) 
   

        
    The_Class.__name__ = 'Vector'

    return The_Class
Vector2D = Vector('xy')
Vector3D = Vector('xyz')
    
    


#v = Vector('xy')
#print(v)

    

