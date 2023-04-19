import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    l, h = 1, max(trees)

    while l <= h:
        mid = (l+h) // 2
        total = sum(tree - mid if tree >= mid else 0 for tree in trees)
        if total >= m:
            l = mid + 1
        else:
            h = mid - 1
    print(h)