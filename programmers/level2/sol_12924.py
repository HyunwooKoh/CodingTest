# 숫자의 표현
def solution(n):
    answer = 1 # 자기 자신
    for i in range(1,n):
        temp = 0
        for j in range(i,n):
            temp += j
            if temp >= n:
                if temp == n:
                    answer += 1
                break
    return answer