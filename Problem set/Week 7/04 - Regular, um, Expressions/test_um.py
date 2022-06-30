from um import count

def test_countum1():
    assert count("um") == 1

def test_countum2():
    assert count("um, ok um...") == 2

def test_countum_symbol():
    assert count("um?") == 1

def test_countum_phrase1():
    assert count("Um, thanks for the album.") == 1

def test_countum_phrase2():
    assert count("Um, thanks, um...") == 2
    
def test_countum_words1():
    assert count("Yummy") == 0

def test_countum_words2():
    assert count("Thats humm, yummy") == 0

def test_countum_words3():
    assert count("Um, good argument") == 1