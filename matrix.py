import logging
import pprint

logger = logging.getLogger(__name__)

def rotate(m, inplace=False):
    '''rotates The Input Matrix By 90 Degrees clockwise. Assumes the input
    matrix is square
    '''
    assert len(m) == len(m[0])
    N = len(m)
    ans = m
    if not inplace:
        ans = [[-1 for x in range(N)] for x in range(N)]

    for layer in range(N//2):
        for i in range(layer, N-1-layer):
            top = m[layer][i]
            right = m[i][N-1-layer]
            bottom = m[N-1-layer][N-1-i]
            left = m[N-1-i][layer]

            ans[layer][i] = left
            ans[i][N-1-layer] = top
            ans[N-1-layer][N-1-i] = right
            ans[N-1-i][layer] = bottom

    return ans


def min_sum_path(M, x=0, y=0, path=None):
    '''Given a m x n grid filled with non-negative numbers, find a path
    from top left to bottom right which minimizes the sum of all numbers
    along its path. Only move down or right.'''
    h, w = len(M), len(M[0])
    path = path or [[-1]*w for row in range(h)]
    if x == h or y == w:
        return float('inf')
    if path[x][y] != -1:
        return path[x][y]
    if x == h-1 and y == w-1:
        return M[x][y]
    path[x][y] = M[x][y] + min(min_sum_path(M, x+1, y, path),
                               min_sum_path(M, x, y+1, path))
    return path[x][y]
