from collections import deque 
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            queue = deque([])
            queue.append(i)
            while queue:
                pos = queue.popleft()
                for j in range(n):
                    if computers[pos][j] == 1 and visited[j] == False:
                        queue.append(j)
                        visited[j] = True
            answer += 1
    return answer