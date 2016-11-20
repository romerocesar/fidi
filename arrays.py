def permute(A, exclude=None):
    '''returns all possible _unique_ permutations of A'''
    exclude = exclude or set()
    seen = set()
    for i, x in enumerate(A):
        if i in exclude:
            continue
        exclude.add(i)
        tail = permute(A, exclude)
        for p in tail:
            t = [x]+p
            seen.add('-'.join([str(y) for y in t]))
        if not tail:
            seen.add(str(x))
        exclude.remove(i)
    ans = []
    for p in seen:
        ans.append([int(x) for x in p.split('-')])
    return ans


def lis(seq):
    '''returns the start and end indices for the longest increasing
    subsequence within the given sequence.'''
    pass


