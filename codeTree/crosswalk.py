# ref https://www.codetree.ai/training-field/frequent-problems/problems/crosswalk
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, l = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        vertLoad = True
        horiLoad = True

        # 열 탐색 (세로)
        last = mat[0][i]
        cnt = 1 # 같은 칸의 개수
        j = 1
        while j < n and vertLoad:
            if mat[j][i] == last:
                cnt += 1
            elif abs(mat[j][i] - last) == 1:
                if last < mat[j][i]:
                    if cnt >= l:
                        last = mat[j][i]
                        cnt = 1
                        continue # 뒤에 도로 설치
                    else:
                        vertLoad = False
                        break
                else: # last > mat[j][i]
                    if j + l > n:
                        vertLoad = False
                        break
                    else:
                        for k in range(j, j+l):
                            if mat[k][i] != mat[j][i]:
                                vertLoad = False
                                break
                        if not vertLoad:
                            break
                        else:
                            # 앞에 도로 설치
                            j += l-1 # 현재 Index를 제외한 앞의 칸 건너뛰기
                            last = mat[j][i]
                            cnt = 0
            else:
                vertLoad = False
            j += 1
        
        # 열 탐색 (가로)
        last = mat[i][0]
        cnt = 1 # 같은 칸의 개수
        j = 1
        while j < n and horiLoad:
            if mat[i][j] == last:
                cnt += 1
            elif abs(mat[i][j] - last) == 1:
                if last < mat[i][j]:
                    if cnt >= l:
                        last = mat[i][j]
                        cnt = 0
                        continue # 뒤에 도로 설치
                    else:
                        horiLoad = False
                        break
                else: # last > mat[i][j]
                    if j + l > n:
                        horiLoad = False
                        break
                    else:
                        for k in range(j, j+l):
                            if mat[i][k] != mat[i][j]:
                                horiLoad = False
                                break
                        if not horiLoad:
                            break
                        else:
                            # 앞에 도로 설치
                            j += l-1 # 현재 Index를 제외한 앞의 칸 건너뛰기
                            last = mat[i][j]
                            cnt = 0
            else:
                horiLoad = False
            j += 1
        if vertLoad:
            res += 1
        if horiLoad:
            res += 1
    print(res)