from itertools import *
from sys import maxsize
import random

def slow(A):
    res = maxsize
    for comb in product(*[[-1, 1]] * len(A)):
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



def test():
    random.seed(a=43)

    for t in range(10**5):
        val = [random.randint(-100, 100) for i in range(5)]
        #print(val)
        s_res, f_res = slow(val), fast(val)
        print('slow: ' + str(s_res))
        print('fast: ' + str(f_res))
        if s_res != f_res:
            print('solution false')
            break


    #print(slow([1, 5, 2, -2]))
    #print(slow([10000, 100, 100, 20]))

if __name__ == '__main__':
    test()