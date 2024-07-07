# Pytest Skip Selective RUn
import Unit_Testing_Introduction
import pytest

@pytest.mark.skip(reason="I don't want to run this test at the moment")
def test_cal_total():
    total = Unit_Testing_Introduction.calc_total(4, 5)
    assert total == 9

import sys

@pytest.mark.skipif(sys.version > (3.5), reason="Because of greater python version")
def test_cal_multiply():
    result = Unit_Testing_Introduction.calc_multiply(4, 5)
    assert result == 20

