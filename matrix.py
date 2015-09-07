import logging

logger = logging.getLogger(__name__)

def rotate(m, inplace=False):
    '''rotates the input matrix by 90 degrees. Assumes the input matrix is
    square'''
    assert len(m) == len(m[0])
    N = len(m)
    # initialize target sequence
    target = []
    ix = N - 1
    last = N*N
    for i in range(N*N):
        target.append(ix)
        ix = ix + N
        # wrap up and to the left
        if last < ix:
            ix = ix % last - 1
    ans = [[-1 for x in range(N)] for x in range(N)]
    for s,t in enumerate(target):
        # source indices
        si = s // N
        sj = s % N
        # target indices
        ti = t // N
        tj = t % N
        # copy
        ans[ti][tj] = m[si][sj]
    return ans
