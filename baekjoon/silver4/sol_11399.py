import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    p = list(sorted(map(int, input().split())))
    dp = [p[0]]
    for i in range(1, num):
        dp.append(dp[i - 1] + p[i])
    print(sum(dp))