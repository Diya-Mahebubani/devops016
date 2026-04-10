from app import add, sub, mul, div
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
def test_sub():
    assert sub(5,2) == 3
    assert sub(0,1) == -1
def test_mul():
    assert mul(2,3) == 6
    assert mul(-1,1) == -1
def test_div():
    assert div(6,2) == 3
    assert div(1,1) == 1