# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import math

def counting(A, o, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in xrange(n):
        if (A[k] > 0 and A[k] < o + m):
            count[A[k] - o] += 1
    return count


def solution(A):
    # write your code in Python 2.7
    
    step_size = 2**22 # about one million
    num_steps = int(math.ceil(2147483647.0 / step_size))
    for i in xrange(num_steps):
        o = i * step_size
        counts = counting(A, o, step_size)
        
        if (i == 0):
            counts[0] = -1
        
        for j, count in enumerate(counts):
            if count == 0:
                return j + o
