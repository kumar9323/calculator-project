from calculator import *

def test_add():
    assert add(10, 5) == 15

def test_addition():
    assert add(1,2) == 3

def test_sub():
    assert sub(10, 5) == 5

def test_subraction():
    assert sub(9,5) == 4

def test_mul():
    assert mul(10, 5) == 50

def test_div():
    assert div(10, 5) == 2

def test_div_by_zero():
    assert div(10, 0) == "Error: Division by zero"