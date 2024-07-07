# Parametrize Test

# To combine multiple test cases into one single test

import module

def test_calc_square_1():
    result = module.calculate_square_area(5)
    assert result == 25


def test_calc_square_2():
    result = module.calculate_square_area(9)
    assert result == 81


def test_calc_square_3():
    result = module.calculate_square_area(10)
    assert result == 100


import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [(5, 25),
                          (9, 81),
                          (10, 100)
                          ]
                         )
def test_calc_square(test_input, expected_output):
    result = module.calculate_square_area(test_input)
    assert result == expected_output


