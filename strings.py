import collections
import logging

logger = logging.getLogger(__name__)

def one_away(first, second):
    '''determine whether the two words are at most one edit away from each
    other'''
    logger.debug(dict(first=first, second=second))
    # no need to compute full edit distance, so we'll just consider
    # some cases.
    distance = 0
    ans = True
    for i,c in enumerate(first):
        if first[i] != second[i]:
            distance += 1
            if len(first) == len(second) + 1:
                second = second[:i] + c + second[i:]
            elif len(first) == len(second) - 1:
                second = second[:i] + second[i+1:]
        if distance > 1:
            ans = False
            break

    logger.info(ans)
    return ans

_ed = collections.defaultdict(dict)
def edit_distance(a, b):
    'https://en.wikipedia.org/wiki/Levenshtein_distance'
    i,j = len(a), len(b)
    if min(i,j) == 0:
        _ed[a][b] = max(i,j)
        return _ed[a][b]
    replace = edit_distance(a[1:], b[1:]) + 1*(a[0] != b[0])
    remove = edit_distance(a[1:], b) + 1
    add = edit_distance(a, b[1:]) + 1
    _ed[a][b] =  min(replace, remove, add)
    return _ed[a][b]
