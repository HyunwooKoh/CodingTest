import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    cups = [int(input()) for _ in range(num)]
    if num == 1:
        print(cups[0])
    elif num == 2:
        print(cups[0] + cups[1])
    else:
        dp = [0] * num
        dp[0] = cups[0]
        dp[1] = cups[0] + cups[1]
        # i 번째의 최대 값 : -2번을 안마시는 경우 / -1번을 안마시는 경우 / i를 안마시는 경우
        dp[2] = max(cups[1] + cups[2], cups[0] + cups[2], dp[1])
        for i in range(3, num):
            dp[i] = max(dp[i-3] + cups[i-1] + cups[i], dp[i-2] + cups[i], dp[i-1])
        print(dp[num-1])