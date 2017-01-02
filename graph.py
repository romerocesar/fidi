import collections
import logging
import strings


logging.basicConfig(level=logging.DEBUG)


class GraphNone(object):
    def __init__(self, v, o=None, i=None):
        self.v = v
        self.i = i or set()
        self.o = o or set()


def dfbnb(node):
    '''Implementation of Depth First Branch and Bound'''
    logging.debug(node)


def neighbors(pair):
    i, j = pair
    yield i+1, j
    yield i, j-1
    yield i-1, j
    yield i, j+1


def bfs(matrix, i=0, j=0, seen=None):
    logging.debug('bfs(seen={})'.format(seen))
    ans = 0
    q = collections.deque()
    q.append((i, j))
    while q:
        pair = q.popleft()
        seen.add(pair)
        for x, y in neighbors(pair):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                continue
            if matrix[x][y] == 'X' and (x, y) not in seen:
                ans += 1
                q.append((x, y))
    return ans


def glyphs(img):
    ans = 0
    seen = set()
    for i, row in enumerate(img):
        for j, px in enumerate(row):
            if px == 'X' and (i, j) not in seen:
                bfs(img, i, j, seen=seen)
                ans += 1
    return ans


def build_graph(words):
    '''builds a graph from an ordered collection of words (e.g. a natural
    language dictionary). There is a node for each unique letter in
    the collection, and an edge from x to y if x < y according to the
    order of the words. The graph is represented by a single
    dictionary with letters as keys and values corresponding to the
    set of letters with incoming edges into the node.
    '''
    ans = collections.defaultdict(set)
    for i in range(1, len(words)):
        prefix = strings.prefix(words[i-1], words[i])
        if len(prefix) < len(words[i]) and len(prefix) < len(words[i-1]):
            x, y = words[i-1][len(prefix)], words[i][len(prefix)]
            ans[y].add(x)
    return ans


def topo_sort(g):
    visited = set()
    q = collections.deque()
    q.extend(g.keys())
    while q:
        node = q.popleft()
        if g[node].difference(visited):
            q.append(node)
        else:
            visited.add(node)
            yield node
