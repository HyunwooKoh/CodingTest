# 멀리 뛰기
# def dfs(idx, n):
#     if idx == n:
#         global ans
#         ans += 1
#     else:
#         if idx + 1 <= n:
#             dfs(idx+1, n)
#         if idx + 2 <= n:
#             dfs(idx+2, n)
    
def solution(n):
    if n <= 2:
        return n
    else:
        dp = [0 for _ in range(n+1)]
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = (dp[i-2] + dp[i-1]) % 1234567
        return dp[n]