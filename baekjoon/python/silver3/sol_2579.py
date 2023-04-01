import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    stairs = [int(input()) for _ in range(num)]
    
    if len(stairs) < 3:
        print(sum(stairs))
    else :
        dp = [0] * num
        dp[0] = stairs[0]
        dp[1] = stairs[0] + stairs[1]
        for i in range(2, num):
            dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
        print(dp[num - 1])