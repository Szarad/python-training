from Window import Window, BorderWindow
from pytest import raises
def test_construct_window_from_corner_width_height():
    w = Window((10,20), (50,60))
    assert type(w) is Window
    assert w.x == 35
    assert w.y == 50
    assert w.height == 60
    assert w.width == 50

    
def x_and_y_should_be_read_only():
    w = Window((11,21), (52,62))
    with raises(AttributeError):
        w.x =0
    with raises(AttributeError):
        w.y =1

def test_area():
    w = Window((12,22),(54,64))
    assert w.area() == 3456

def test_perimeter():
    w = Window((13,23),(56,66))
    assert w.perimeter() == 244
def test_constructor_from_corners():
    w = Window.from_corners((100,200), (600, 400))
    assert w.x == 350
    assert w.y == 300
    assert w.width == 500
    assert w.height == 200

def test_border_window_area_xy_wh_main_constructor():
    w = BorderWindow((10,20), (50,60))
    assert type(w) is BorderWindow
    assert w.x == 35
    assert w.y == 50
    assert w.width == 60
    assert w.height == 70
def test_area_with_borders():
    w = BorderWindow((12,22), (54,64))
    assert w.area() == 4736
def test_construct_from_corners_border_window():
    w = BorderWindow.from_corners((100,200), (600, 400))
    assert w.x == 350
    assert w.y == 300
    assert w.width == 510
    assert w.height == 210


#def test_border_window_height_includes_border():

