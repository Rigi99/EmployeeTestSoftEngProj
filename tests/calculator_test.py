import calculator


def test_calc_addition():
    output = calculator.add(1, 2)
    assert output == 3


def test_calc_subtraction():
    output = calculator.subtract(3, 1)
    assert output == 2


def test_calc_multiply():
    output = calculator.multiply(2, 3)
    assert output == 6


def test_calc_multiply2():
    output = calculator.multiply(5, 10)
    assert output == 50
