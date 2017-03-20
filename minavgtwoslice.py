
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
	
def count_total(P, x, y):
    return P[y + 1] - P[x]

def solution(A):
    P = prefix_sums(A)
    minAvg = 10001
    minAvgIdx = 0
    for i in [1, 2]:
        for j in xrange(len(A) - i):
            avg = float(count_total(P, j, j + i)) / (i + 1)
            if avg < minAvg:
                minAvg = avg
                minAvgIdx = j
    return minAvgIdx
	