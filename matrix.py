import logging
import pprint

logger = logging.getLogger(__name__)

def rotate(m, inplace=False):
    '''rotaTes The Input Matrix By 90 Degrees clockwise. Assumes the input
    matrix is square
    '''
    assert len(m) == len(m[0])
    N = len(m)
    ans = m
    if not inplace:
        ans = [[-1 for x in range(N)] for x in range(N)]

    for layer in range(N//2):
        for i in range(layer,N-1-layer):
            top = m[layer][i]
            right = m[i][N-1-layer]
            bottom = m[N-1-layer][N-1-i]
            left = m[N-1-i][layer]

            ans[layer][i] = left
            ans[i][N-1-layer] = top
            ans[N-1-layer][N-1-i] = right
            ans[N-1-i][layer] = bottom

    return ans
