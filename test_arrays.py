import random
import arrays

def test_permute():
    # arrange
    A = [1,1,2]
    # act
    p = arrays.permute(A)
    # assert
    assert sorted(p) == [[1,1,2],[1,2,1],[2,1,1]]


def test_min_jumps():
    assert arrays.min_jumps([2, 3, 1, 1, 4]) == 2
    assert arrays.min_jumps([33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28]) == 3


def test_celebrity():
    # arrange
    N = random.randint(9, 99)
    guests = list(range(N))
    celeb_idx = random.randint(0, N-1)
    # act
    no_celeb = arrays.celebrity(guests, lambda i, j: True if i == j else False)
    celeb = arrays.celebrity(guests, lambda i, j: True if i == j or j == celeb_idx else False)
    # assert
    assert celeb == celeb_idx
    assert no_celeb == -1

def test_triangles():
    assert arrays.triangles([1, 1, 1, 2, 2]) == 4