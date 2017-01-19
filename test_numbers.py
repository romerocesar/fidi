import logging
import numbers

logging.basicConfig(level=logging.DEBUG)


def test_square():
    assert numbers.square(11) == 3
    assert numbers.square(0) == 0
    assert numbers.square(4) == 2
    assert numbers.square(848311266) == 29125


def test_sieve():
    assert numbers.sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_fib():
    assert numbers.fib(4) == 5


def test_prices2560():
    assert [4.0, 1.0, 6.0] == numbers.round_prices([1.48, 3.49, 5.6])
