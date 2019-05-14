from pytest import mark

from hypothesis            import given
from hypothesis.strategies import floats

sensible_floats = floats(min_value=0.1, max_value=1e3, allow_nan=False, allow_infinity=False)
FLOATS = sensible_floats

from Particle import Particle

@given(FLOATS, FLOATS, FLOATS, FLOATS, FLOATS)
def test_Particle_constructor_should_set_basic_attributes(r,x,y,vx,vy):
    p = Particle(r, (x,y), (vx,vy))
    assert p.r  ==  r
    assert p.x  ==  x
    assert p.y  ==  y
    assert p.vx == vx
    assert p.vy == vy
