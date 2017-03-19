import itertools
from sys import maxsize, setrecursionlimit
import random

def slow(A):
    res = maxsize
    for comb in itertools.product(*[[-1, 1]] * len(A)):
        temp = abs(sum([x * y for x, y in zip(A, comb)]))
        #print(temp)
        res = min(res, temp)
    return res

def step(current_sum, dp, possibs):
    possibs = [x for x in possibs if current_sum - 2 * x >= 0]
    res = maxsize
    for i, x in enumerate(possibs):
        #print(x)
        new = current_sum - 2 * x
        if dp[new] is False:
            dp[new] = True
            res = min(res, new, step(new, dp, possibs[:i] + possibs[i + 1:]))
    return res

def fast(A):
    A = sorted([abs(x) for x in A], reverse=True)
    total = sum(A)
    max_elem = A[0]
    dp = [False] * (total + 1)
    return step(total, dp, A)

    if False:
        res = maxsize
        for comb in product(*[[-1, 1]] * len(A)):
            current_sum = total
            for i, c in enumerate(comb):
                if c == -1:
                    new = current_sum - 2 * A[~i]
                    if new >= 0:
                        if dp[new]:
                            break
                        else:
                            dp[new] = True
                            current_sum = new
                            res = min(res, current_sum)



        #temp = abs(sum([x * y for x, y in zip(A, comb)]))
        #print(temp)
        #if not dp[temp]:
        #    dp[temp] = True
        #    unique_count += 1
        # print(temp)
        #res = min(res, temp)
        #print(unique_count)
        return res

def step2(current_sum, count, dp):
    res = maxsize
    for i in reversed(range(len(count))):
        if count[i] >= 1:
            new = current_sum - 2 * i
            if new >= 0 and dp[new] is False:
                dp[new] = True
                count[i] -= 1
                res = min(res, new, step2(new, count, dp))
                count[i] += 1
    return res

def fast2(A):
    A = [abs(x) for x in A]
    count = [0] * (max(A) + 1)
    total = 0
    for x in A:
        total += x
        count[x] += 1
    dp = [False] * (total + 1)
    return step2(total, count, dp)

def fast3(A):
    A = [abs(x) for x in A]
    count = [0] * (max(A) + 1)
    total = 0
    for x in A:
        total += x
        count[x] += 1
    dp = [False] * (total + 1)
    res = maxsize

    stack = [(total, -1)]
    while stack:
        current_sum, to_remove = stack.pop()
        if current_sum != -1: # code for finish of depth traversal
            if to_remove != -1:
                count[to_remove] -= 1
            for i in range(len(count)):
                if count[i] >= 1:
                    new = current_sum - 2 * i
                    if new >= 0 and dp[new] is False:
                        dp[new] = True
                        res = min(res, new)
                        if res == 0:
                            return res
                        stack.append((-1, i))
                        stack.append((new, i))
        elif to_remove != -1:
            count[to_remove] += 1
    return res

def test():
    random.seed(a=43)

    setrecursionlimit(30000)

    for t in range(10**2):
        val = [random.randint(-100, 100) for i in range(5)]
        print(val)
        #print(fast3(val))
        s_res, f_res, f2_res, f3_res = slow(val), fast(val), fast2(val), fast3(val)
        print('slow: ' + str(s_res))
        print('fast: ' + str(f_res))
        print('fast2: ' + str(f2_res))
        print('fast3: ' + str(f3_res))
        if s_res != f_res or s_res != f2_res or s_res != f3_res:
            print('solution false')
            break


    #print(slow([1, 5, 2, -2]))
    #print(slow([10000, 100, 100, 20]))

if __name__ == '__main__':
    test()