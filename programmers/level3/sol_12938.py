def solution(n, s):
    if n > s:
        return [-1]
    answer = []
    qt = s // n
    for _ in range(n):
        answer.append(qt)
    it = len(answer) -1
    for _ in range(s % n):
        answer[it] += 1
        it -= 1
    return answer