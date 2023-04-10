import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    sums = [0]
    for _ in range(m):
        i, j = map(int, input().split())
        if j >= len(sums):
            for k in range(len(sums), j + 1):
                sums.append(sums[k-1] + nums[k-1])
        print(sums[j] - sums[i - 1])