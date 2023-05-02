import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x,y):
    queue = []
    queue.append((x,y))

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] != 1:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            
    print(graph[n-1][m-1])


if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))
    bfs(0,0)
    