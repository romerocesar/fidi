import strings
import pytest

def test_one_away():
    # add char
    first='pale'
    second='ple'
    assert strings.one_away(first, second)
    # replace one char
    second = 'bale'
    assert strings.one_away(first, second)
    # remove a char
    second = 'pales'
    assert strings.one_away(first, second)
    # two edits
    second='bake'
    assert not strings.one_away(first, second)

def test_edit_distance():
    # arrange
    a = 'kitten'
    b = 'sitting'
    assert strings.edit_distance(a,b) == 3
