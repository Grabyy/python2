import pytest

def test_one_plus_one():
    assert 1 + 1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

#@pytest.mark.parametrize('a, b, product', product)
#def test_multiplication(a, b, product):
   # assert a * b == product


