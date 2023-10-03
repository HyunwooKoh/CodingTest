import sys
sys.setrecursionlimit(int(1e9))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0

def dfs(board, visited, x, y, cnt, chance):
    hasMove = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= 4 and 0 <= ny <= 4 and not visited[ny][nx]:
            if board[y][x] < board[ny][nx]:
                hasMove = True
                visited[ny][nx] = True
                dfs(board, visited, nx, ny, cnt+1, chance)
                visited[ny][nx] = False
            elif chance and board[y][x] > board[ny][nx]:
                hasMove = True
                visited[ny][nx] = True
                dfs(board, visited, nx, ny, cnt+1, False)
                visited[ny][nx] = False
    
    if not hasMove:
        global answer
        answer = max(answer, cnt)
    
def solution(board):
    for i in range(5):
        for j in range(5):
            visited = [[False]*5 for _ in range(5)]
            visited[i][j] = True
            dfs(board, visited, j, i, 1, True)

    global answer
    return answer