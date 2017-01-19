import math


def fib(n):
    if n < 2:
        return 1
    a, b, c = 1, 1, 2
    for i in range(n-2):
        a, b, c = b, c, b+c
    return c

# prices = [1.18, 3.19, 5.6, 7.501]
# sum(prices) = 10.57
# final price = $11
# constraint 1: sum(your_rounded_prices) == final price
# constraint 2: minimize sum(rounding_error) for all prices
# rounding_error = abs(original_price - rounded_line_item)
def round_prices(prices):
    final_price = round(sum(prices))
    rounded = []
    deltas = []
    for x in prices:
        r = round(x)
        rounded.append(r)
        deltas.append(r-x)
    _total = sum(rounded)
    if _total == final_price:
        return rounded
    diff = final_price - _total
    ans = []
    for d, r in sorted(zip(deltas, rounded), reverse=True, key=lambda x: abs(x[0])):
        if not diff or diff/abs(diff) == d/abs(d):
            ans.append(r + 0)
        else:
            ans.append(r + diff/abs(diff))
            diff = diff - diff/abs(diff)
    return ans
        

def fac(n):
    ans = 1
    for i in range(2, n+1):
        ans = ans * i
    return ans


def sieve(n):
    primes = []
    seen = [0] * (n//64 + 1)
    for i in range(2, n):
        bit = seen[i // 64] & (1 << (i % 64))
        if not bit:
            primes.append(i)
            j = i
            while j < n:
                seen[j // 64] |= 1 << (j % 64)
                j += i
    return primes


def primes(n):
    ans = set()
    for i in range(2, n):
        prime = True
        for p in ans:
            if i % p == 0:
                prime = False
                break
        if prime:
            ans.add(i)
    return ans


def primesum(n):
    _primes = sieve(n)
    for p in _primes:
        if n - p in _primes:
            return [p, n - p]


def square(n):
    if n < 2:
        return n
    i = 2
    while i * i <= n:
        i += i
    l, u = i // 2, i
    c = (l + u) // 2
    while c != l:
        s = c * c
        if s == n:
            return c
        elif s > n:
            u = c
        else:
            l = c
        c = (l + u) // 2
    return c
            
        
