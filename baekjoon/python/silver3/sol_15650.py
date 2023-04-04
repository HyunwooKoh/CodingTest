import sys
input = sys.stdin.readline

def dfs(l : list, n, m, start):
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(start, n + 1):
        if i not in l:
            l.append(i)
            dfs(l, n, m, i)
            l.pop()

if __name__ == "__main__":
    n, m = map(int,input().split())
    l = []
    dfs(l, n, m, 1)