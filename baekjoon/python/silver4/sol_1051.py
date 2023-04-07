import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = []

    for i in range(n):
        array.append(list(input()))

    check = min(n, m)
    size = 0
    for i in range(n):
        for j in range(m):
            for k in range(check):
                if ((i + k) < n) and ((j + k) < m) and (array[i][j] == array[i][j + k] == array[i + k][j] == array[i + k][j + k]):
                    size = max(size, (k + 1)**2)

    print(size)