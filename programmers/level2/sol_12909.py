def solution(s):
    answer = True
    cnt = 0
    for ch in s:
        if ch == '(':
           cnt +=1
        else:
            cnt -= 1
        if cnt < 0:
            answer = False
            break
    if cnt != 0:
        answer = False
    return answer