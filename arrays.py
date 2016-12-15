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


def min_jumps(A, start=0, jumps=None):
    '''Given an array of non-negative integers, you are initially
    positioned at the first index of the array. Each element in the
    array represents your maximum jump length at that position. Your
    goal is to reach the last index in the minimum number of jumps.'''
    ans = -1
    jumps = jumps or [-1]*len(A)
    if jumps[start] != -1:
        return jumps[start]
    if start == len(A) - 1:
        return 0
    for step in range(A[start], 0, -1):
        _start = start+step
        if _start >= len(A):
            continue
        _jumps = min_jumps(A, _start, jumps)
        if _jumps == -1:
            continue
        if ans == -1:
            ans = _jumps + 1
        else:
            ans = min(ans, _jumps + 1)
    jumps[start] = ans
    return jumps[start]


def celebrity(guests, knows):
    i, j = 0, 1
    while j < len(guests) and i < len(guests):
        if knows(guests[i], guests[j]):
            i = max(i, j) + 1
        else:
            j = max(i, j) + 1
    # validate celeb status
    celeb = guests[min(i, j)]
    for guest in guests:
        if not knows(guest, celeb):
            return -1
    return celeb

def triangles(A):
    A.sort()
    ans = 0
    for h in range(len(A)-1, 1, -1):
        l, m = 0, h-1
        while l != m:
            if A[l] + A[m] > A[h]:
                ans += m - l
                m = m - 1
            else:
                l += 1
        
    return ans
