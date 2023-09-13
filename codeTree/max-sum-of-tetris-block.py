import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 모든 연속된 4칸은 주어진 동형 내에 있음
# -> 연속된 4칸의 최대 합을 구하는 문제
def dfs(x, y, total, depth):
    global res
    if depth == 4:
        res = max(res, total)
    elif total + maxValue * (4 - depth) < res:
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if not visited[ny][nx]:
                if depth == 1:
                    # ㅗ 모양 탐색

                visited[ny][nx] = True
                dfs(nx, ny, total + mat[ny][nx], depth+1)
                visited[ny][nx] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = 0
    maxValue = 0
    visited = [[False]*m for _ in range(n)]
    
    mat = []
    for _ in range(n):
        line = list(map(int, input().split()))
        maxValue = max(maxValue, max(line))
        mat.append(line)

    for y in range(n):
        for x in range(m):
            dfs(x,y,0,0)
    
    print(res)