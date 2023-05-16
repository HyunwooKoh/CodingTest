import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    p = list(map(int, input().split()))
    p.insert(0,0)
    dp = [0] * (num+1)

    for i in range(1, num+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i], p[j] + dp[i-j])
    print(dp[num])