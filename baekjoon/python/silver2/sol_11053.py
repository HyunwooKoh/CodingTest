import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    a = list(map(int, input().split()))
    dp = [0] * num
    for i in range(num):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))