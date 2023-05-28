import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = [i for i in range(n + 1)]
        
    for _ in range(m):
        opr, a, b = map(int, input().split())
        if opr == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")