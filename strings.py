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
    for i, c in enumerate(first):
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
    logger.debug(dict(a=a, b=b))
    if b in _ed[a]:
        logger.info('found {}'.format(_ed[a][b]))
        return _ed[a][b]
    i, j = len(a), len(b)
    if min(i, j) == 0:
        _ed[a][b] = max(i, j)
        logger.info(_ed[a][b])
        return _ed[a][b]
    replace = edit_distance(a[1:], b[1:]) + 1*(a[0] != b[0])
    remove = edit_distance(a[1:], b) + 1
    add = edit_distance(a, b[1:]) + 1
    _ed[a][b] = min(replace, remove, add)
    logger.info(_ed[a][b])
    return _ed[a][b]


def longest_prefix(a, b):
    'returns the longest prefix common to both strings'
    if not a or not b:
        return ''
    for i, c in enumerate(a):
        if len(b) <= i:
            return b
        if b[i] != c:
            return a[:i]
    return a


def suffix_similarities(word):
    '''calculates the sum of similarities of a string S with each of its
    suffixes, including the string itself as the first suffix'''
    ans = len(word)
    for i in range(1, len(word)):
        for j in range(i, len(word)):
            if word[j] != word[j-i]:
                ans += j-i
                break
        else:
            ans += len(word) - i
    return ans


def prefix(a, b):
    'returns the longest prefix common to both strings'
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]
        

class Trie():

    def __init__(self, words):
        if type(words) == str:
            self.symbol = words[0]
            self.terminal = len(words) == 1
            self.children = {self.symbol: Trie(words[1:])}
        elif type(words) == list:
            self.symbol = ''
            self.children = {}
            self.terminal = False
            for word in words:
                c = word[0]
                self.children[c] = Trie(word[1:])

    def add(self, word):
        pass
