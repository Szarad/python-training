from functools import partial, wraps
# _ - one value that not caring about 

def repport_result(fun):
		def dec_fun(*args, **kwords):
			result = fun(*args, **kwords)
			print(result)
		return dec_fun
	 


def repport_args(func):
		@wraps(func)
		def decoreted_func(*args, **kwords):
			print(args, kwords)
			return func(*args, *kwords)
		return	decoreted_func


# repport_args = repport_args(badd)
#@repport_result
#repport_result = repport_args(badd(a,b))
@repport_args
def badd(a,b):
	"bad addition"
	return a * b
print(badd(2,3))
'''
def eins(_):
    return 1

#def inc(n):
#	return n+1
''' 
#factory of functions. 
#carrying rewritting multiarguments function to chain of single arguments function 

def add(a,b):
	return a+b

class INC_BY:
	def __init__(self, n):
		self.n = n

	def __call__(self, n):
		return self.n + n 


def inc_by(n):
	def inc(m):
		return n+m
	return inc

add3 = inc_by(3)
print(add3(10))
print(dir(add3))


# cannot put @add, it needs 2 parameters
#partial functolls
#part_func = functools.partial(add,10)

@partial(add, 10)
@INC_BY(10)
@inc_by(10) # parametrized
@inc
@eins
def bonjour():
    return 'hello'

xxx = INC_BY(10)
bonjour = xxx(bonjour)


#bonjour = eins(bonjour)
print(bonjour)
'''
