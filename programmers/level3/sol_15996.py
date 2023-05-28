from collections import Counter

def solution(weights):
    answer = 0
    c = Counter(weights)
    for i in weights:
        c[i] -= 1
        if i in c:
            answer += c[i]
        if i * 2 in c:
            answer += c[i*2]
        if i / 2 in c:
            answer += c[i/2]
        if i * 3 / 2 in c:
            answer += c[i*3/2]
        if i * 2 / 3 in c:
            answer += c[i*2/3]
        if i * 4 / 3 in c:
            answer += c[i*4/3]
        if i * 3 / 4 in c:
            answer += c[i*3/4]
        c[i] += 1
    return answer //2