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
        
