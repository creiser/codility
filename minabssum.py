import itertools
from sys import maxsize, setrecursionlimit
import random
from time import perf_counter

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
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return abs(A[0])
    A = [abs(x) for x in A]  # sign doesn't matter for this problem
    count = [0] * (max(A) + 1)  # compress by counting, allows space efficient 'recursive' calls
    total = 0
    for x in A:
        total += x
        count[x] += 1
    dp = [False] * (total + 1)  # save already visited absolute sums
    res = maxsize

    # depth first search, always subtract the highest available numbers first
    # use stack to emulate recursive function calls
    stack = [(total, -1)]  # start with no numbers subtracted
    while stack:
        current_sum, to_remove = stack.pop()
        if current_sum != -1:  # magic number that makes to_remove available again
            if to_remove != -1:
                count[to_remove] -= 1
            for i in range(len(count)):  # this order is actually reversed by the stack, so it is highest to lowest
                if count[i] >= 1:
                    new = current_sum - 2 * i
                    if new >= 0 and dp[new] is False:  # only positive sums are considered, that weren't visited yet
                        dp[new] = True
                        res = min(res, new)
                        if res == 0:
                            return res
                        stack.append((-1, i))  # -1 = magic number that makes 'i' available again
                        stack.append((new, i))  # in the 'call' below 'i' won't be available
        elif to_remove != -1:
            count[to_remove] += 1
    return res

def test():
    random.seed(a=43)

    setrecursionlimit(30000)

    for t in range(10**2):
        val = [random.randint(-100, 100) for i in range(7)]
        print()
        #print(val)
        res = -1
        fail = False
        for algo in [slow, fast3]:
            start = perf_counter()
            nres = algo(val)
            if nres != res and res != -1:
                print('fail! ' + str(res) + ' ' + str(nres))
                fail = True
                break
            res = nres
            end = perf_counter()
            print(algo.__name__ + ': ' + str(end - start) + ' ' + str(res))
        if fail:
            break

if __name__ == '__main__':
    test()