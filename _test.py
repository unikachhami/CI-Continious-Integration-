import pytest

def square(n):
    return n**2
def cube(n):
    return n**3
def fifth(n):
    return n**5

def test_square():
    assert square(2) == 4,"Square of 2 is 4: Test Failed"
    assert square(3) == 9,"Cube of 3 is 9: Test Failed"


def test_cube():
    assert cube(2) == 8,"Cube of 2 is 8: Test Failed"
    assert cube(3) == 27,"Cube of 3 is 27: Test Failed"

def test_fifth():
    assert fifth(2) == 32,"Fifth of 2 is 32: Test Failed"
    assert fifth(3) == 32,"Fifth of 3 is 243: Test Failed"

def test_invalid_input():
    with pytest.raises(TypeError):
        square('string')




