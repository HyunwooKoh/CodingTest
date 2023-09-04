# 카펫
def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yHeight = yellow / i
            if i * 2 + yHeight * 2 + 4 == brown:
                return [yHeight + 2, i + 2]