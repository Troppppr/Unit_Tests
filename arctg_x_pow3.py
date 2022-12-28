import math

def arctg_x_pow3(x):
    return math.atan(x) + x**3

def arctg_x(x):
    return math.atan(x)

def test_arctg_x_pow3():
    assert abs(arctg_x_pow3(0) - 0) < 1e-9
    assert abs(arctg_x_pow3(1) - 1.328038074) < 1e-9
    assert abs(arctg_x_pow3(-1) + 1.328038074) < 1e-9
    assert abs(arctg_x_pow3(2) - 3.638682504) < 1e-9
    assert abs(arctg_x_pow3(-2) + 3.638682504) < 1e-9
    assert abs(arctg_x_pow3(3) - 7.797301647) < 1e-9
    assert abs(arctg_x_pow3(-3) + 7.797301647) < 1e-9
    assert abs(arctg_x_pow3(4) - 14.50339619) < 1e-9
    assert abs(arctg_x_pow3(-4) + 14.50339619) < 1e-9
    assert abs(arctg_x_pow3(5) - 24.80856863) < 1e-9
    assert abs(arctg_x_pow3(-5) + 24.80856863) < 1e-9
    assert abs(arctg_x_pow3(0.5) - 0.84148248) < 1e-9
    assert abs(arctg_x_pow3(-0.5) + 0.84148248) < 1e-9
    assert abs(arctg_x_pow3(1.5) - 2.367076593) < 1e-9
    assert abs(arctg_x_pow3(-1.5) + 2.367076593) < 1e-9
    assert abs(arctg_x_pow3(2.5) - 4.881044124) < 1e-9
    assert abs(arctg_x_pow3(-2.5) + 4.881044124) < 1e-9
    assert abs(arctg_x_pow3(3.5) - 9.283440847) < 1e-9
    assert abs(arctg_x_pow3(3.5) - 9.283440847) < 1e-9
    assert abs(arctg_x_pow3(4.5) - 15.69085448) < 1e-9
    assert abs(arctg_x_pow3(-4.5) + 15.69085448) < 1e-9
    test_arctg_x_pow3()

def test_arctg_x():
    assert abs(arctg_x(0) - 0) < 1e-9
    assert abs(arctg_x(1) - 0.785398163) < 1e-9
    assert abs(arctg_x(-1) + 0.785398163) < 1e-9
    assert abs(arctg_x(2) - 1.107148718) < 1e-9
    assert abs(arctg_x(-2) + 1.107148718) < 1e-9

test_arctg_x()

def x_pow3(x):
    return x**3

def test_x_pow3():
    assert abs(x_pow3(0) - 0) < 1e-9
    assert abs(x_pow3(1) - 1) < 1e-9
    assert abs(x_pow3(-1) - -1) < 1e-9
    assert abs(x_pow3(2) - 8) < 1e-9
    assert abs(x_pow3(-2) - -8) < 1e-9

test_x_pow3()
