from Interval import Interval

x1 = Interval(0.9, 1.1)
x2 = Interval(1.999, 2.001)
x3 = Interval(-1, 1)
x4 = Interval(10, 10)

def test_add():
    assert x1 + x2 == Interval(2.899, 3.101)

def test_sub():
    assert x3 - x4 == Interval(-11, -9)

def test_mul():
    assert x2 * x3 == Interval(-2.001, 2.001)

def test_div():
    assert x3 / x4 == Interval(-0.1, 0.1)

def test_complex_equation():
    assert x4-x1*x2/(x4+x3)-(x1+x2)== Interval(6.6544333333333325, 6.937445454545455)

def test_intersect():
    assert x1.intersect(x3) == Interval(0.9, 1)

def test_intersects():
    assert x1.intersects(x3) == True
    assert x1.intersects(x2) == False

def test_exceptions():
    try:
        x4 / x3
    except Exception as err:
        assert str(err) == 'interval division by zero'
    try:
        a = Interval(2, -2)
    except Exception as err:
        assert str(err) == 'empty interval'
