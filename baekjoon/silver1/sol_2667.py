import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(px, py):
    count = 0
    queue = []
    queue.append((px, py))

    while queue:
        x, y = queue.pop(0)
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 0:
                continue
            graph[nx][ny] = 0
            queue.append((nx, ny))

    return count

if __name__ == "__main__":  
    n = int(input())
    graph = []
    counts = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                graph[i][j] = 0
                counts.append(bfs(i,j))
    
    counts.sort()
    print(len(counts))
    for c in counts:
        print(c)