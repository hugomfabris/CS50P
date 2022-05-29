from fcntl import F_GETLEASE
from plates import is_valid

def test_is_valid_true_strings1():
    assert is_valid("HELLO") == True

def test_is_valid_true_strings2():
    assert is_valid("HI") == True

def test_is_valid_false_strings1():
    assert is_valid("H") == False

def test_is_valid_false_strings2():
    assert is_valid("OUTATIME") == False

def test_is_valid_numbers1():
    assert is_valid("1984") == False

def test_is_valid_numbers2():
    assert is_valid("3.14") == False

def test_is_valid_alphanumeric1():
    assert is_valid("CS50") == True

def test_is_valid_alphanumeric2():
    assert is_valid("CS05") == False

def test_is_valid_alphanumeric3():
    assert is_valid("PI3.14") == False

def test_is_valid_alphanumeric4():
    assert is_valid("HB33C") == False

def test_is_valid_alphanumeric5():
    assert is_valid("HBC34") == True

def test_is_valid_alphanumeric6():
    assert is_valid("12ABCD") == False

def test_is_valid_alphanumeric7():
    assert is_valid("ECTO88") == True

def test_is_valid_alphanumeric8():
    assert is_valid("NRVOUS") == True

def test_is_valid_alphanumeric9():
    assert is_valid("A7") == False

    
     
 