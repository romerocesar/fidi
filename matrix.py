from collections import defaultdict
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def rotate(m, inplace=False):
    '''rotates The Input Matrix By 90 Degrees clockwise. Assumes the input
    matrix is square
    '''
    assert len(m) == len(m[0])
    N = len(m)
    ans = m
    if not inplace:
        ans = [row[:] for row in m]

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


def boggle(words, n):
    '''given words, generate an nxn board of boggle where every row and
    column contains a valid word when read forward or backward'''
    words = set(words)
    candidates = {word for word in words if len(word) == n and reversed(word) in words}
    # start with empty board


def valid_sudoku(board):
    columns = [defaultdict(int) for i in range(9)]
    rows = [defaultdict(int) for i in range(9)]
    matrices = [[defaultdict(int) for i in range(3)] for j in range(3)]
    # aggregate by set
    for i in range(9):
        for j in range(9):
            rows[i][board[i][j]] += 1
            columns[j][board[i][j]] += 1
            matrices[i//3][j//3][board[i][j]] += 1
    # validate sets
    for i in range(9):
        for k, v in columns[i].items():
            if k != '.' and v > 1:
                return False
        for k, v in rows[i].items():
            if k != '.' and v > 1:
                return False
        x, y = i//3, i % 3
        for k, v in matrices[x][y].items():
            if k != '.' and v > 1:
                return False
    return True


def max_sum_square_submat(a, b):
    '''Given a 2D integer matrix A of size N x N find a B x B submatrix
    where B<= N and B>= 1, such that sum of all the elements in submatrix
    is maximum.'''
    ans = float('-inf')
    N = len(a)
    cols = a[:]
    for x in range(N*N):
        row = x//N
        col = x%N
        if row:
            cols[row][col] += cols[row-1][col]

    for x in range(0, N*N):
        row = x//N
        col = x%N
        if col + b > N:
            continue
        if row + b > N:
            break
        cumsum = sum(cols[row+b-1][col:col+b])
        if row:
            cumsum -= sum(cols[row-1][col:col+b])

        ans = max(ans, cumsum)

    return ans
