import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# dfs 쓰면 시간 초과
def dfs(idx, sums):
    if sums == k:
        global res
        res += 1
        return
    elif sums > k or idx == n:
        return

    if sums + coins[idx] <= k:
        dfs(idx, sums + coins[idx])
    dfs(idx + 1, sums)

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [0] * (k+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            dp[i] += dp[i-coin]
    print(dp[k])