# ref https://www.codetree.ai/training-field/frequent-problems/problems/war-finish
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    total = 0
    mat = []
    
    for i in range(n):
        line = list(map(int, input().split()))
        mat.append(line)
        total += sum(line)

    res = int(1e9)

    for x0 in range(1, n-1):
        print("x0 : " + str(x0))
        for y0 in range(n-1, 1, -1):
            print("y0 : " + str(y0))
            for length in range(2, y0):
                print("length : " + str(length))
                for right in range(1, length -1):
                    print("right : " + str(right))
                    left = length - right
                    
                    x1, y1 = x0 + right, y0+right
                    if x1 >= n or y1 >= n:
                        break

                    x2, y2 = x0 + (right-left), y0+ length
                    if x2 < 0 or x2 >= n or y2 < 0:
                        break
                    
                    x3, y3 = x0 - left, y0 + left
                    if x3 <0 or y3 >= n:
                        break

                    countries = [0]

                    # 2번 나라 인구수 계산
                    humans = 0
                    for y in range(0,y3):
                        for x in range(x2 + 1 if y > y2 else x2 - (y - y2)):
                            humans += mat[y][x]
                    countries.append(humans)

                    # 3번 나라 인구수 계산
                    humans = 0
                    for y in range(y1):
                        for x in range(x2 + 1 if y <= y2 else x2 + 1 - (y - y2), n):
                            humans += mat[y][x]
                    countries.append(humans)

                    # 4번 나라 인구수 계산
                    humans = 0
                    for y in range(y3, n):
                        for x in range(x0 -1 if y >= y0 else x0 - 1 - (y0 - y)):
                            humans += mat[y][x]
                    countries.append(humans)

                    # 5번 나라 인구수 계산
                    humans = 0
                    for y in range(y1 + 1, n):
                        for x in range(x0 if y > y0 else x0 - (y0 - y) - 1):
                            humans += mat[y][x]
                    countries.append(humans)

                    # 1번 나라 인구수 계산
                    countries[0] = total - sum(countries)
                    print("countries : " + str(countries))
                    print()
                    res = min(res, max(countries) - min(countries))
    
    print(res)