import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    count = 0
    for i in range(n-1, -1, -1):
        count += k // coins[i]
        k = k % coins[i]
        if k == 0:
            break
    print(count)