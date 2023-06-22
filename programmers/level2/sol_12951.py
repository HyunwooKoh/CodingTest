def solution(s):
    tokens = s.split(' ')
    for i in range(len(tokens)):
        tokens[i] = tokens[i].capitalize()
    answer = ' '.join(tokens)
    return answer