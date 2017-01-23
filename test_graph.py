import graph
import logging

logging.basicConfig(level=logging.DEBUG)


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


def test_successors():
    # arrange
    words = ['hot', 'hit', 'cog', 'dot', 'dog', 'lot', 'log']
    # act
    actual = graph.successors(words)
    # assert
    assert 'hot' in actual['hit']
    assert len(actual['cog']) == 2
    assert len(actual['dog']) == 3


def test_succ():
    assert graph.succ('hit', 'hot')
    assert not graph.succ('hit', 'dog')


def test_word_ladder():
    # arrange
    words = ['hot', 'dot', 'dog', 'lot', 'log']
    start = 'hit'
    end = 'cog'
    expected = (True, [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']])
    # act
    actual = graph.word_ladder(start, end, words)
    # assert
    assert actual == expected
    assert graph.word_ladder('bb', 'bb', ['bb'])[1] == [['bb']]
    # arrange
    words = ['baba', 'abba', 'aaba', 'bbbb', 'abaa', 'abab', 'aaab', 'abba', 'abba', 'abba', 'bbba', 'aaab', 'abaa', 'baba', 'baaa']
    start = 'bbaa'
    end = 'babb'
    actual = graph.word_ladder(start, end, words)
    logging.debug(actual)
    assert 0
