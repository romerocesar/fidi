import matrix


def test_min_sum():
    # arrange
    M = [
        [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
    ]
    # act
    s = matrix.min_sum_path(M)
    # assert
    assert s == 8
    # arrange
    M = [
        [20, 29, 84, 4, 32, 60, 86, 8, 7, 37],
        [77, 69, 85, 83, 81, 78, 22, 45, 43, 63],
        [60, 21, 0, 94, 59, 88, 9, 54, 30, 80],
        [40, 78, 52, 58, 26, 84, 47, 0, 24, 60],
        [40, 17, 69, 5, 38, 5, 75, 59, 35, 26],
        [64, 41, 85, 22, 44, 25, 3, 63, 33, 13],
        [2, 21, 39, 51, 75, 70, 76, 57, 56, 22],
        [31, 45, 47, 100, 65, 10, 94, 96, 81, 14]
    ]
    assert 470 == matrix.min_sum_path(M)


def test_rotate():
    # arrange
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    # act
    actual = matrix.rotate(m)
    # assert
    assert expected == actual


def test_valid_sudoku():
    # arrange
    invalid = [[1]*9 for i in range(9)]
    valid = ["53..7....",
             "6..195...",
             ".98....6.",
             "8...6...3",
             "4..8.3..1",
             "7...2...6",
             ".6....28.",
             "...419..5",
             "....8..79"]
    # assert
    assert matrix.valid_sudoku(valid)
    assert not matrix.valid_sudoku(invalid)
