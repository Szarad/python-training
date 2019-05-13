def mydir(x):
	return dir(x)


class Foo:
    def meth(*args):
        return args 
    @staticmethod
    def static(*args):
        return args
    static = staticmethod(static)
   
    @classmethod 
    def class_(*args):
        return args
    class_ = classmethod(class_)
    dir = dir
    mir = mydir



# binding behaviors of class methods:
print(Foo().class_())
print(Foo.class_())

print (Foo().static())
print (Foo. static())

# bonding behaviors doesn't exists for static method

print(Foo().meth())
print(Foo.meth())
# function implemented in C, doesn't have binding via instance
print(Foo().dir())
# binidn because of the python function
print(Foo().mir())
######

def f(a,b,*args):
	return a,b,args

print(f(1,2))
print(f(1,2))
print(f(*"hello"))


def f(a,**kwds):
        return a,kwds


x= dict(b=2, a=9)
print(f(**x)) # f(b=2, a=9)


def f(a,b,c,**kwds):
	return a,b,c,kwds

x = dict(b=2,a=9,banana=19)
f(c=6, d=8, **x)


#### function could take anything as an argument:
def f(*args, **kwds):
	blah
	g(*args, **kwds)
	sth






'''
def f(a,b,**kwds):
        return a,b,args

print(f(1,2))
   '''          
