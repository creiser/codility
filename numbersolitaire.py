from sys import maxsize

def solution(A):
    for i in range(1, len(A)):
        m = -maxsize - 1
        for j in range(1, 7):
            if i - j >= 0:
                m = max(m, A[i - j])
        A[i] = A[i] + m
    return A[-1]


# shorter
def solution(A):
    for i in range(1, len(A)):
        A[i] = A[i] + max(A[max(0, i - 6): i])
    return A[-1]