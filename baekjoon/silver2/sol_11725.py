import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(idx):
    for i in tree[idx]:
        if parent[i] == -1:
            parent[i] = idx
            dfs(i)


if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n)]
    parent = [-1] * n

    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    
    dfs(0)
    
    for i in range(1, n):
        print(parent[i] + 1)