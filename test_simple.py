def multi(a,b):
	return a*b
def test_multiplicationfunction_with_three_pairs():
	for(l,r,x) in ((2,3,6), (3,-1, -3), (0.5, 0.5, 0.25)):
		assert multi(l,r) == x



