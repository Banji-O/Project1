# Selective Test

import Unit_Testing_Introduction
import pytest

@pytest.mark.windows  # testing as windows  pytest -m windows -v
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac  # testing as mac pytest -m mac -v
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True