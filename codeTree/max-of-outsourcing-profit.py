# 삼성 SW역량 테스트 기출문제 - 외주 수익 최대화하기
# ref https://www.codetree.ai/training-field/frequent-problems/problems/max-of-outsourcing-profit/
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0 for _ in range(n+1)]
    job = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-1, -1, -1):
        if i + job[i][0] <= n:
            dp[i] = max(dp[i + job[i][0]] + job[i][1], dp[i+1])
        else:
            dp[i] = dp[i+1]

    print(dp[0])