from fib import fib, fibi
from pytest import mark
from hypothesis import given
from hypothesis.strategies import integers

parametrize = mark.parametrize

# @example
@given(integers(min_value=2, max_value=1000))
def test_fib_should_be_sum_of_previous_two(n):
	assert fibi(n) == fibi(n-1) + fibi(n-2)

'''
@parametrize('fib', (fib, fibi))
@parametrize('i, o', ((0,0), (1,1),(3,2)))
def test_fib_of_should_give_results(i,o, fib):
    	assert fib(i) == o  '''
