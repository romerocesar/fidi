import heapq
import logging


def chocolates(k, A):
    ans = 0
    heap = [-1 * x for x in A]
    heapq.heapify(heap)
    while k:
        logging.debug(heap)
        n = heapq.heappop(heap) * -1
        ans = ans + n
        heapq.heappush(heap, n//2 * -1)
        k = k - 1
    return ans % 1000000007
