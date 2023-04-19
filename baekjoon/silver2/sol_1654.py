import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k, n = map(int, input().split())
    lines = [int(input()) for _ in range(k)]

    l,h = 1, sum(lines) // k
    while l <= h:
        mid = (l + h) // 2
        total = sum([line // mid for line in lines])
        if total >= n:
            l = mid + 1
        else:
            h = mid - 1
    print(h)