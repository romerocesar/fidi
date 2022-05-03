import collections
from functools import reduce
import logging


def zero(puzzle):
    n = len(puzzle)
    for i in range(n):
        for j in range(n):
            if not puzzle[i][j]:
                return i,j


def move(puzzle, direction=None):
    n = len(puzzle)
    r,c = zero(puzzle)
    # now move if valid
    if direction == 'u' and r:
        puzzle[r][c], puzzle[r-1][c] = puzzle[r-1][c], puzzle[r][c]
        return True, puzzle[r][c]
    elif direction == 'l' and c:
        puzzle[r][c], puzzle[r][c-1] = puzzle[r][c-1], puzzle[r][c]
        return True, puzzle[r][c]
    elif r<n-1 and direction=='d':
        puzzle[r][c], puzzle[r+1][c] = puzzle[r+1][c], puzzle[r][c]
        return True, puzzle[r][c]
    elif c<n-1 and direction=='r':
        puzzle[r][c], puzzle[r][c+1] = puzzle[r][c+1], puzzle[r][c]
        return True, puzzle[r][c]
    else:
        return False, -1


def goal(puzzle):
    n = len(puzzle)
    ordered = list(range(n*n))[1:]+[0]
    flattened = reduce(lambda x,y:x+y, puzzle)
    return ordered == flattened


def dfs(puzzle, bound=1):
    logging.warn(bound)
    if goal(puzzle):
        return True, []
    elif not bound:
        return False, []
    for d in 'urdl':
        b, n = move(puzzle,d)
        if b:
            g, p = dfs(puzzle, bound-1)
            if g:
                return g, [n]+p
    return False, []


def dfid(puzzle):
    bound = 1
    while True:
        g, path = dfs(puzzle, bound)
        if g:
            return path
        else:
            bound += 1


def slide_puzzle(puzzle):
    return dfid(puzzle)
