def solution(A):
    A.sort()
    if A[0] >= 0:
        return 2 * A[0] # all positive numbers
    if A[-1] <= 0:
        return abs(2 * A[-1]) # all negative numbers
    left, right = 0, len(A) - 1
    res = abs(A[left] + A[right])
    while A[left] < 0:
        while A[right] > 0 and abs(A[left] + A[right - 1]) < abs(A[left] + A[right]):
            right -= 1
            res = min(res, abs(A[left] + A[right]))
        left += 1
        res = min(res, abs(A[left] + A[right]))
    if left > 0:
        res = min(res, abs(2 * A[left - 1])) #  negative number with smallest absolute val
    res = min(res, abs(2 * A[left])) # positive number with smallest absolute val or zero
    return res