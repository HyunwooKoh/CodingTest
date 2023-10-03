def solution(contests, k, p):
    answer = [i for i in range(len(contests))]
    prob4Con = {}

    for i in range(len(contests)):
        cnt = 0
        for j in range(len(contests[i])):
            if contests[i][j] <= p:
                cnt += 1
        prob4Con[i] = cnt
    
    answer.sort(key = lambda x : (-prob4Con[x], x))
    return sorted(answer[0:k])