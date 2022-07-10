import pytest
from seasons import check_birthday, date_dealing

def test_date_dealing1():
    assert(date_dealing('2021-07-09')) == 'Five hundred twenty-five thousand, six hundred minutes'

def test_date_dealing2():
    with pytest.raises(SystemExit):
        assert date_dealing('2021-07-9') == 'Invalid date'

def test_date_dealing3():
    assert(date_dealing('1936-10-11')) == 'Forty-five million, ninety-six thousand, four hundred eighty minutes'