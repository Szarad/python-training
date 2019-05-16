from math   import sqrt

from hypothesis            import given
from hypothesis.strategies import integers

#@give(integers)
def test_raiserror():
    v = ValueError()
    assert sqrt(-1) == v 
