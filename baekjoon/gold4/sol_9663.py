import sys
input = sys.stdin.readline

def isPromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    if x == n:
        global res
        res += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        
        row[x] = i
        if isPromising(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False

res = 0
if __name__ == "__main__":
    n = int(input())
    row = [0] * n
    visited = [False] * n

    dfs(0)
    print(res)