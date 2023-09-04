import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    
    res = 0
    for i in range(N):
        # 가로 길 확인하기
        horizLoad = True
        lastHeight = mat[i][0]
        hisCount = 1
        degreeway = [False for _ in range(N)] 
        for j in range(1, N):
            if mat[i][j] == lastHeight:
                hisCount += 1
            elif mat[i][j] == lastHeight - 1:
                # 발판이 맵을 벗어나는지
                if L > N - j:
                    horizLoad = False
                    break
                else:
                    canLoad = True
                    for k in range(j, j+L):
                        if mat[i][k] != mat[i][j]:
                            canLoad = False
                            break
                        degreeway[k] = True
                    if not canLoad:
                        horizLoad = False
                        break
                    else:
                        hisCount = 1
                        lastHeight = mat[i][j]
            elif mat[i][j] == lastHeight + 1:
                # 지나온 같은 칸의 개수 >= L이고, 현재칸 ~ -L 까지 발판이 있는지
                if hisCount >= L:
                    canLoad = True
                    for k in range(j-1, j-L-1 ,-1):
                        if degreeway[k]:
                            canLoad = False
                            break
                        degreeway[k] = True
                    if canLoad:
                        hisCount = 1
                        lastHeight = mat[i][j]
                    else:
                        horizLoad = False
                        break
                else:
                    horizLoad = False
                    break
            else:
                horizLoad = False
                break
        
        
        # 세로 길 확인하기
        verticLoad = True
        lastHeight = mat[0][i]
        hisCount = 1
        degreeway = [False for _ in range(N)]
        for j in range(1, N):
            if mat[j][i] == lastHeight:
                hisCount += 1
            elif mat[j][i] == lastHeight - 1:
                # 발판이 지도를 벗어나는지
                if L > N - j:
                    verticLoad = False
                    break
                else:
                    # 앞에 칸을 검사하면서 발판 설치
                    canLoad = True
                    for k in range(j, j + L):
                        if mat[k][i] != mat[j][i]:
                            canLoad = False
                            break
                        degreeway[k] = True
                    if not canLoad:
                        verticLoad = False
                        break
                    else:
                        hisCount = 1
                        lastHeight = mat[j][i]
            elif mat[j][i] == lastHeight + 1:
                # 지나온 같은 칸의 개수 >= L이고, 현재칸 ~ -L 까지 발판이 있는지
                if hisCount >= L:
                    canLoad = True
                    for k in range(j-1, j-L-1 ,-1):
                        if degreeway[k]:
                            canLoad = False
                            break
                        degreeway[k] = True
                    if canLoad:
                        hisCount = 1
                        lastHeight = mat[j][i]
                    else:
                        verticLoad = False
                        break
                else:
                    verticLoad = False
                    break
            else:
                verticLoad = False
                break
        
        #print("i : " + str(i) + ", horizLoad : " + str(horizLoad))
        #print("i : " + str(i) + ", verticLoad : " + str(verticLoad))
        #print()
        
        if horizLoad:
            res += 1
        if verticLoad:
            res += 1
    print(res)