# 야근 지수
minRes = 1e9
def dfs(work, remain):
    if remain == 0:
        #print(work)
        global minRes
        res = 0
        for w in work:
            res += w*w
        #print(res)
        minRes = min(minRes, res)
    else:
        for i in range(len(work)):
            if work[i] > 1:
                work[i] -= 1
                dfs(work, remain-1)
                work[i] += 1
import heapq
def solution(n, works):
    res = 0
    if sum(works) > n:
        works = [-w for w in works]
        heapq.heapify(works)
        for _ in range(n):
            temp = heapq.heappop(works)
            temp += 1
            heapq.heappush(works, temp)
        res = sum([w ** 2 for w in works])
    return res