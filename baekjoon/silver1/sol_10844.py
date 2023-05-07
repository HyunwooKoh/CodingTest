import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    dp = [[0] * 10 for _ in range(num)]
    dp[0] = [0,1,1,1,1,1,1,1,1,1]

    for i in range(1, num):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
    
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[num-1]) % 1000000000)