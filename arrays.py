import collections
import numbers
import logging

from collections import defaultdict


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


def count_unique_permutations(A):
    '''returns the number of unique permutations that can be generated
    with the elements in A'''
    num = numbers.fac(len(A))
    d = defaultdict(int)
    for x in A:
        d[x] += 1
    den = 1
    for v in d.values():
        den = den * numbers.fac(v)
    return num//den


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


def equal(A):
    '''Given an array A of integers, find the index of values that satisfy
    A + B = C + D, where A,B,C & D are integers values in the array'''
    idx = defaultdict(list)
    for i, v in enumerate(A):
        idx[v].append(i)
    for a in range(len(A)):
        for b in range(a+1, len(A)):
            for c in range(a+1, len(A)):
                if b == c:
                    continue
                v = A[a] + A[b] - A[c]
                for d in idx.get(v, []):
                    if d > c and d != b:
                        return [a, b, c, d]
    return []


def bulbs(A):
    ans = 0
    curr = -1
    for bulb in A:
        if not bulb and not ans:
            ans = 1
            curr = 0
        elif not bulb and curr != bulb:
            ans += 1
            curr = bulb
        elif bulb and ans and bulb != curr:
            ans += 1
            curr = bulb
    return ans


def highest_product(A):
    A.sort()
    a, b, c = A[-3:]
    return max(a*b*c, A[0]*A[1]*A[-1])


def candies(A):
    candies = [-1] * len(A)
    children = sorted([(rating, pos) for pos, rating in enumerate(A)])
    for rating, pos in children:
        if candies[pos] != -1:
            continue
        candies[pos] = 1
        j = pos - 1
        while j >= 0 and A[j] > A[j + 1]:
            candies[j] = max(candies[j + 1] + 1, candies[j])
            j -= 1
        j = pos + 1
        while j < len(A) and A[j] > A[j - 1]:
            candies[j] = max(candies[j - 1] + 1, candies[j])
            j += 1

    return sum(candies)


def merge_overlaps(intervals):
    intervals.sort()
    ans = []
    interval = None
    for s, e in intervals:
        if not interval:
            interval = [s, e]
        elif interval[1] >= s:
            interval[1] = max(e, interval[1])
        else:
            ans.append(tuple(interval))
            interval = [s, e]
    ans.append(tuple(interval))
    return ans


def set_zeros(A):
    row = 0 if 0 in A[0] else 1
    col = 0 if 0 in [r[0] for r in A] else 1
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                A[0][j] = 0
                A[i][0] = 0

    for r in range(1, len(A)):
        if A[r][0] == 1:
            continue
        for c in range(len(A[0])):
            A[r][c] = 0
    for c in range(1, len(A[0])):
        if A[0][c] == 1:
            continue
        for r in range(len(A)):
            A[r][c] = 0

    if not row:
        for c in range(len(A[0])):
            A[0][c] = 0
    if not col:
        for r in range(len(A)):
            A[r][0] = 0

    return A


def unique_numbers(A, k):
    d = collections.defaultdict(int)
    for i in range(k):
        d[A[i]] += 1
    count = len(d.keys())
    ans = [count]
    i = 0
    for j in range(k, len(A)):
        d[A[i]] -= 1
        if not d[A[i]]:
            count -= 1
        d[A[j]] += 1
        if d[A[j]] == 1:
            count += 1
        ans.append(count)
        i += 1
    return ans


def bin_search(A, x):
    l, u = 0, len(A) - 1
    c = (l + u) // 2
    while c != l:
        if A[c] == x:
            return c
        elif A[c] > x:
            u = c
        else:
            l = c
        c = (l + u) // 2

    if A[l] >= x:
        return l
    elif A[l] < x <= A[u]:
        return u
    else:
        return u + 1

    
def max_sub_array(a):
    'finds the contiguous subarray of a'
    ans = float('-inf')
    cumsum = float('-inf')
    for i,x in enumerate(a):
        if cumsum > 0:
            cumsum += x
        else:
            cumsum = max(cumsum, x)
        ans = max(ans, cumsum)
    
    return ans


def first_missing_positive(a):
    'a is unsorted, find the first missing positive integer. expect O(n) time and O(n) space'
    a = set(a)
    for x in range(1, len(a)+2):
        if x not in a:
            return x

def first_missing_positive(a):
    'a is unsorted, find the first missing positive integer. expect O(n) time and O(1) space.'
    for i in range(len(a)):
        v = a[i]
        while 0 < v < len(a)+1 and a[v-1] != v:
            tmp = a[v-1]
            a[v-1] = v
            v = tmp
    for i,x in enumerate(a):
        if x != i+1:
            return i+1
    return len(a)+1

