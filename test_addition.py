from add import add_numbers

def test_positive_no():
    assert add_numbers(10,40) == 50

def test_zero():
    assert add_numbers(10,0) == 10

def test_negitive_no():
    assert add_numbers(-10,20) == 10