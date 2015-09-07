import pytest
import matrix

def test_rotate():
    # arrange
    a = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    b = [
        [13,9,5,1],
        [14,10,6,2],
        [15,11,7,3],
        [16,12,8,4]
    ]
    # act
    c = matrix.rotate(a)
    # assert
    assert b == c
    assert c != a
    # act inplace
    c = matrix.rotate(a, inplace=True)
    assert b == c == a
