from twttr import shorten

def test_shorten_titled1():
    assert shorten('Twitter ') == "Twttr"

def test_shorten_titled2():
    assert shorten('Good Lucky') == "Gd Lcky"

def test_shorten_lower():
    assert shorten('good morning, friend.') == "gd mrnng, frnd."

def test_shorten_upper():
    assert shorten('HI FRIEND') == "H FRND"

def test_shorten_number():
    assert shorten('CS50') == 'CS50'