if __name__ == "__main__" :
    n, m = map(int, input().split())
    origin = []
    count = []

    for _ in range(n):
        origin.append(input())

    for a in range(0, n-7):
        for b in range(0, m-7):
            # 판 짜르기
            wCount = 0
            bCount = 0
            # 색칠 계산
            for i in range(a, a+8):
                for j in range(b, b+8):
                    if (i+j) % 2 == 0:
                        if origin[i][j] != 'W':
                            wCount += 1
                        if origin[i][j] != 'B':
                            bCount += 1
                    else:
                        if origin[i][j] != 'B':
                            wCount += 1
                        if origin[i][j] != 'W':
                            bCount += 1
            count.append(min(wCount, bCount))

    print(min(count))