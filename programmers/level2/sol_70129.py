# 이진 변환 반복하기
def solution(s):
    answer = [0,0]
    while True:
        if s == "1":
            break
        lenCount = 0
        zeroCount = 0
        for i in range(len(s)):
            if s[i] == "1":
                lenCount += 1
            else:
                zeroCount += 1

        s = str(format(lenCount, 'b'))
        
        answer[0] += 1
        answer[1] += zeroCount
    return answer