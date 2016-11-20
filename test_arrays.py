import arrays

def test_permute():
    # arrange
    A = [1,1,2]
    # act
    p = arrays.permute(A)
    # assert
    assert sorted(p) == [[1,1,2],[1,2,1],[2,1,1]]
