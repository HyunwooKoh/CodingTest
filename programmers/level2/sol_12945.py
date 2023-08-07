# 피보나치 수
def solution(n):
    dp = [0,1]
    if n > 1:
        for i in range(2,n):
            dp.append(dp[i-2] + dp[i-1])    
        return (dp[n-2] + dp[n-1]) % 1234567
    else:
        return dp[n]