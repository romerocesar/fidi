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
    a = 'kitten'
    b = 'sitting'
    assert strings.edit_distance(a,b) == 3
    # arrange
    a = 'ababababab'
    b = 'bababababa'
    assert strings.edit_distance(a,b) == 2


def test_longet_prefix():
    assert strings.longest_prefix('aaa', 'aaab') == 'aaa'
    assert strings.longest_prefix('abc', 'abd') == 'ab'


def test_prefix():
    assert strings.prefix('aaa', 'aaab') == 'aaa'
    assert strings.prefix('abc', 'abd') == 'ab'


def test_suffix_similarities():
    assert strings.suffix_similarities('ababaa') == 11
    assert strings.suffix_similarities('aa') == 3
