import sys
input = sys.stdin.readline

def dfs(start, temp):
    if len(temp) == m:
        print(' '.join(map(str,temp)))
        return
    for i in range(start, n):
            temp.append(nums[i])
            dfs(i, temp)
            temp.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    temp = []

    dfs(0, temp)