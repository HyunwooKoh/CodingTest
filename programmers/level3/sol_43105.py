from collections import deque
def dfs(triangle, steps, depth):
    if depth == len(triangle):
        global maxRes
        maxRes = max(maxRes, sum(steps))
        return
    else:
        idx = triangle[depth-1].index(steps[depth-1])
        for i in range(2):
            steps.append(triangle[depth][idx + i])
            dfs(triangle, steps, depth +1)
            steps.pop()
        
def solution1(triangle):
    global maxRes
    maxRes = 0
    
    dfs(triangle, deque([triangle[0][0]]), 1)
    return maxRes



def solution2(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[len(triangle)-1])
