def solution(s):
    # map -> 튜플로 변환
    # list -> 튜플을 다시 리스트로 변환
    l = list(map(int, s.split(' ')))
    answer = str(min(l)) + ' ' + str(max(l))
    return answer