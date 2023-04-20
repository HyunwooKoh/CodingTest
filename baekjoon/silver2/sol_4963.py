import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

def dfs(x, y):
    graph[y][x] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or ny >= h or nx >= w:
            continue
        elif graph[ny][nx] == 1:
            dfs(nx, ny)

if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        
        count = 0
        for y in range(h):
            for x in range(w):
                if graph[y][x] == 1:
                    dfs(x, y)
                    count += 1
        print(count)
        #print("count : " + str(count))