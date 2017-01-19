import graph
import logging


def test_glyphs():
    # arrange
    img = [
        '000000',
        '0XX000',
        '0XX000',
        '000000',
        '0XXXXX'
    ]
    # act
    actual = graph.glyphs(img)
    # assert
    assert actual == 2


def test_build_graph():
    # arrange
    words = ['airplane', 'beach', 'castro', 'cesar', 'desert', 'empanada']
    # act
    g = graph.build_graph(words)
    # assert
    assert g == {'d': {'c'}, 'e': {'a', 'd'}, 'b': {'a'}, 'c': {'b'}}


def test_topo_sort():
    # arrange
    g = {'a': set(), 'd': {'c'}, 'e': {'a', 'd'}, 'b': {'a'}, 'c': {'b'}}
    # act
    assert list(graph.topo_sort(g)) == ['a', 'b', 'c', 'd', 'e']


