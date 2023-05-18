import sys

input = sys.stdin.readline
MAX = 0

def dfs(weight, value, size, idx):
    if idx >= len(stock) or weight + stock[idx][0] > k:
        global MAX
        MAX = max(MAX, value)
        return
    else:
        dfs(weight + stock[idx][0], value + stock[idx][1], size, idx+1)
        dfs(weight, value, size, idx+1)

if __name__ == "__main__" :
    n, k = map(int, sys.stdin.readline().split())
    # DFS
    #  stock = []
    # for _ in range(n):
    #     w ,v = map(int, input().split())
    #     if w <= k:
    #         stock.append([w, v])
    # stock.sort()
    # dfs(0,0,len(stock),0)
    # print(MAX)

    stock = [(0, 0)]
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for _ in range(n):
        stock.append(list(map(int, input().split())))

    for i in range(1, n + 1):
         for j in range(1, k + 1):
            w = stock[i][0]
            v = stock[i][1]
            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[n][k])