def gauss(n):
    return (n * (n + 1)) // 2

def solution(M, A):
    count = [0] * (M + 1)
    lim = 1000000000
    left = right = res = 0
    while right < len(A):
        while right < len(A) and count[A[right]] == 0:
            count[A[right]] = 1
            right += 1
        if res != lim:
            res += gauss(right - left)
        if right < len(A):
            while A[left] != A[right]:
                count[A[left]] = 0
                left += 1
            count[A[left]] = 0
            left += 1
            res -= gauss(right - left)
        res = min(lim, res)
    return res