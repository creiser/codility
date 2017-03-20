from math import sqrt, floor

def solution(A):
    if len(A) < 3:
        return 0
    if len(A) == 3:
        return 1 if A[0] < A[1] and A[1] > A[2] else 0
        
    peaks = [-1] * len(A)
    lastPeak = -1
    for i in reversed(xrange(1, len(A) - 1)):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            lastPeak = i
        peaks[i] = lastPeak
    peaks[0] = peaks[1]
    
    if peaks[0] == -1:
        return 0
        
    #print(peaks)
    
    maxNumFlags = 1
    K = 2
    while K <= floor(sqrt(len(A))) + 1:
        #print ('K: ' + str(K))
        numFlags = 1
        current = peaks[0]
        while numFlags < K:
            #print('current: ' + str(current))
            current = min(len(A) - 1, current + K)
            #print('current: ' + str(current))
            if current == -1: break
            current = peaks[current]
            if current == -1: break
            numFlags = numFlags + 1
        #print('(end) current: ' + str(current))
        #print('numFlags: ' + str(numFlags))
        maxNumFlags = max(maxNumFlags, numFlags)
        K = K + 1
    
    return maxNumFlags