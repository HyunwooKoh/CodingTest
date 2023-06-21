import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, hisLen):
    global maxNum
    maxNum = max(maxNum, hisLen)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and not mat[ny][nx] in history:
            history.add(mat[ny][nx])
            dfs(nx, ny, hisLen + 1)
            history.remove(mat[ny][nx])    
    

if __name__ == "__main__":
    r, c = map(int, input().split())
    global maxNum
    maxNum = 0
    mat = []
    for _ in range(r):
        mat.append(list(input()))
    history = {mat[0][0]}
    dfs(0,0,1)
    print(maxNum)