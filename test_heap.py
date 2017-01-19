import heaps
import logging

logging.basicConfig(level=logging.DEBUG)


def test_chocolates():
    # trivial
    k = 3
    A = [6, 5]
    assert heaps.chocolates(k, A) == 14
    # non-trivial
    k = 10
    A = [2147483647, 2000000014, 2147483647]
    assert heaps.chocolates(k, A) == 284628164
