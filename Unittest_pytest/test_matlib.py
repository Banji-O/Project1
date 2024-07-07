import Unit_Testing_Introduction

def test_calc_total():
    total = Unit_Testing_Introduction.calc_total(4, 5)
    assert total == 9

def test_calc_multiply():
    result = Unit_Testing_Introduction.calc_multiply(4, 5)
    assert result == 20


