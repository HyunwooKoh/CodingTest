# 다음 큰 숫자
def solution(n):
    oneCount = str(format(n, 'b')).count('1')
    while True:
        n += 1
        if str(format(n, 'b')).count('1') == oneCount:
            break
    return n