from working import convert
import pytest

def test_working_valid1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_working_valid2():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_working_valid3():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'

def test_working_valid4():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_working_valid_12():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

def test_working_valid_12():
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'

def test_working_valid_12():
    assert convert('12:25 AM to 12:01 PM') == '00:25 to 12:01'

def test_working_invalid1():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 5:60')

def test_working_invalid2():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')

def test_working_invalid3():
    with pytest.raises(ValueError):
        assert convert('09:00 AM - 17:00')