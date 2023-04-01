import sys
input = sys.stdin.readline

def dfs(l, n, m):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, n + 1):
        if i not in l:
            l.append(i)
            dfs(l, n, m)
            l.pop()

if __name__ == "__main__":
    n, m = map(int,input().split())
    l = []
    dfs(l, n, m)