import numbers


def test_fib():
    assert numbers.fib(4) == 5


def test_prices():
    assert [4.0, 1.0, 6.0] == numbers.round_prices([1.48, 3.49, 5.6])
