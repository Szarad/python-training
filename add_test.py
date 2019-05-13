from hypothesis import given
from hypothesis.strategies import integers

'''
def secret(a,b):
	if b==0:
		return a
	if a==0:
		return b
	return 3
'''

def secret(a,b):
	if a > 1000: return 777
	return a +b


@given(integers(),integers())
def test_commutativity(a,b):
	assert secret(a,b) == secret(b,a)

@given(integers())
def test_identity_is_zero(a):
    assert secret(a,0) == a 

@given(integers(),integers(),integers() )
def test_associativity(a,b,c):
    assert secret(a,secret(b,c)) == secret(secret(a,b),c)




