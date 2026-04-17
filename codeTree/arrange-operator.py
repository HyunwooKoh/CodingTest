# ref https://www.codetree.ai/training-field/frequent-problems/problems/arrange-operator
import sys
input = sys.stdin.readline

def dfs(sums, idx, plusCnt, minusCnt, multiCnt):
    if idx == n:
        global maxRes
        global minRes
        maxRes = max(maxRes, sums)
        minRes = min(minRes, sums)
        return
    if plusCnt > 0:
        dfs(sums + nums[idx], idx+1, plusCnt-1, minusCnt, multiCnt)
    if minusCnt > 0:
        dfs(sums - nums[idx], idx+1, plusCnt, minusCnt-1, multiCnt)
    if multiCnt > 0:
        dfs(sums * nums[idx], idx+1, plusCnt, minusCnt, multiCnt-1)

if __name__ == "__main__":
    maxRes = 1e9 * -1
    minRes = 1e9
    n = int(input())
    nums = list(map(int, input().split()))
    plusCnt, minusCnt, multiCnt = map(int, input().split())
    dfs(nums[0], 1, plusCnt, minusCnt, multiCnt)

    print(str(int(minRes)) + " " + str(int(maxRes)))