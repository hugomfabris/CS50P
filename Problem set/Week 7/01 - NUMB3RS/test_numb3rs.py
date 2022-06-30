from numb3rs import validate

def test_validate_numbers1():
    assert validate('121.131.144.152') == True

def test_validate_numbers2():
    assert validate('1.1.144.12') == True

def test_validate_numbers3():
    assert validate('1.0.0.150') == True

def test_validate_numbers3():
    assert validate('1.2.1.1500') == False

def test_validate_numbers4():
    assert validate('1.0.0.0') == True

def test_validate_numbers5():
    assert validate('0.1.0.0') == True

def test_validate_numbers6():
    assert validate('1.275.1003.767') == False

def test_validate_numbers7():
    assert validate('277.11.104.76') == False

def test_validate_numbers8():
    assert validate('1.275.1.1') == False

def test_validate_numbers9():
    assert validate('1.1.275.1') == False

def test_validate_numbers9():
    assert validate('1.1.1.275') == False

def test_validate_string1():
    assert validate('dog.cat.abc.cs50') == False

def test_validate_string2():
    assert validate('cat') == False

def test_validate_alphanumeric():
    assert validate('2001:0db8:85a3:0000:0000:8a2e:0370:7334') == False