from fuel import convert, gauge
import pytest

def test_convert_correct_fraction1():
    assert convert('3/4') == 75

def test_convert_correct_fraction2():
    assert convert('5/25') == 20

def test_convert_incorrect_fraction():
    with pytest.raises(ValueError):
        assert convert('5/4') == "X can't be greater than Y"

def test_convert_incorrect_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert('4/0') == "Y can't be zero"

def test_gauge_correct_e():
    assert gauge(1) == 'E'

def test_gauge_correct_f():
    assert gauge(99) == 'F'

def test_gauge_correct_int1():
    assert gauge(75) == '75%'

def test_gauge_correct_int2():
    assert gauge(47) == '47%'

