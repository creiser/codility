from collections import deque
from bisect import bisect_right

def solution(A):
    b = sorted([(x[0] - x[1], x[0] + x[1]) for x in enumerate(A)], key=lambda x: x[0])
    l = deque([x[0] for x in b])
    num = 0
    for i in xrange(len(b)):
        l.popleft()
        idx = bisect_right(l, b[i][1])
        num = num + (idx if idx != -1 else 0)
    return num if num <= 10000000 else -1