import npuzzle

def test_small():
    puzzle = [
        [4,1,3],
        [2,8,0],
        [7,6,5]
    ]
    solution == npuzzle.dfid(puzzle)
    print(solution)


def test_medium():
    puzzle = [
        [10, 3, 6, 4],
        [ 1, 5, 8, 0],
        [ 2,13, 7,15],
        [14, 9,12,11]
    ]
    solution = npuzzle.dfid(puzzle)
    print(solution)


def test_large():
    puzzle = [
        [ 3, 7,14,15,10],
        [ 1, 0, 5, 9, 4],
        [16, 2,11,12, 8],
        [17, 6,13,18,20],
        [21,22,23,19,24]
    ]
    solution = npuzzle.dfid(puzzle)
    print(solution)
