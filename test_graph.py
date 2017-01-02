import graph


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

