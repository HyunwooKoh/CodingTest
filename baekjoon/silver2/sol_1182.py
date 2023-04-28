import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(idx, sets : list):
    if sum(sets) == s and len(sets) > 0 :
        global count
        count += 1
    elif s >= 0 and sum(sets) > s:
        return

    for i in range(idx, len(nums)):
        sets.append(nums[i])
        dfs(i+1, sets)
        sets.pop()

if __name__ == "__main__":
    global count
    count = 0
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    dfs(0, [])
    print(count)