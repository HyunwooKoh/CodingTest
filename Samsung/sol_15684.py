import sys
input = sys.stdin.readline

def check():
    for line in range(n):
        pos = line
        for j in range(h):
            if graph[pos][j] != -1:
                pos = graph[pos][j]
        
        if pos != line:
            return False
    return True


def dfs(cnt, line, pos):
    global res
    if 3 < cnt or res <= cnt:
        return
    elif check():
        res = cnt
    else:
        for i in range(line, n-1): #마지막 라인은 X
            for j in range(pos if i == line else 0, h):
                if graph[i][j] == -1 and graph[i+1][j] == -1:
                    graph[i][j] = i+1
                    graph[i+1][j] = i
                    dfs(cnt+1, i, j)
                    graph[i][j] = -1
                    graph[i+1][j] = -1


if __name__ == "__main__":
    n,m,h = map(int, input().split())
    graph = [[-1] * h for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        graph[b][a] = b+1
        graph[b+1][a] = b
    res = 4
    dfs(0, 0 ,0)
    print(res if res <= 3 else -1)
