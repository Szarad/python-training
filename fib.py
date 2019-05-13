def fib(n):
	return 1

def fibi(n):
	if n<2: return n
	c = 1
	p = 0
	while n>1:
		c,p = c + p, c
		n -= 1 		
	return c

print(fibi(0))
print(fibi(1))
print(fibi(2))
