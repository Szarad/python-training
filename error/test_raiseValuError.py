from math   import sqrt

from hypothesis            import given
from hypothesis.strategies import integers
from pytest import raises
from contextlib import contextmanager
#@give(integers)
def test_raiserror():
    try:
        sqrt(-1)
    except ValueError:
        assert True
    except:
        assert False
    else:
        assert False

'''
raises(ValueError, sqrt(-1)) - couldn't not work, because exception is called and raises() won't start

'''
def test_raise_error_pytest_ugly():
    raises(ValueError, sqrt, -1)
    raises(ValueError, lambda:sqrt(-1))

def test_raise_error_pytest_bad():
    raises(ValueError, 'sqrt(-1)')


def test_raise_error_pytest_good():
    with raises(ValueError):
        sqrt(-1)


@contextmanager
def my_raises(spec):
    try:
        yield
    except spec:
        assert True
    except:
        assert False
    else:
        assert False




'''
def test_raise_error_pytest():
    with raises(ValueError, match="Value cannot be negative"):
        raise ValueError("Value cannot be negative")
def test_raises_error_pytest():
    with raises(ValueError) as error_value:
        if value < 0:
            raise ValueError("value must be not negative")
        asser error_value.type is ValueError
'''
