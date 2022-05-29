from bank import value

def test_value():
    assert value("Hello, how can I help you?") == 0
    assert value("hello, hello") == 0

def test_value2():
    assert value("Hi, friend") == 20
    assert value("How are you?") == 20

def test_value3():
    assert value("What's up?") == 100
    assert value("1") == 100