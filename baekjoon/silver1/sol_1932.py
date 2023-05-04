import sys
input = sys.stdin.readline

if __name__ == "__main__" :
    # 현재 층에서 전 층의 max(idx -1, idx) + 값
    # 마지막 라인에서의 MAX값 추출
    num = int(input())
    graph = []
    for _ in range(num):
        graph.append(list(map(int, input().split())))
    
    for i in range(1, num):
        for j in range(i + 1):
            if j == 0:
                graph[i][j] += graph[i-1][j]
            elif j == i:
                graph[i][j] += graph[i-1][j-1]
            else:
                graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

    print(max(graph[num-1]))