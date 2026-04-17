# ref https://www.codetree.ai/training-field/frequent-problems/problems/rabit-and-race
import sys
import heapq
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

if __name__ == "__main__":
    q = int(input())
    cmd = list(map(int, input().split()))
    n, m, p = cmd[1], cmd[2], cmd[3]
    rabit = {0 : []} # key : 점프 횟수 , value : [(행번호+열번호, 행번호, 열번호, 고유 번호)]
    rabitDist = [0 for _ in range(int(1e7))] # 토끼(pid) 별 점프 거리
    rabitMinusScore = [0 for _ in range(int(1e7))] # 토끼(pid) 별, 이동해서 못 받은 점수
    rabitPlusScore = [0 for _ in range(int(1e7))]  # 토끼(pid) 별, 추가로 받은 점수
    minJump = 0 # 최소 점프 횟수 보관
    totalScore = 0

    # 토끼 정보 입력
    for i in range(4, len(cmd), +2):
        heapq.heappush(rabit[0], (0, 0, 0, cmd[i])) # 토끼 좌표 init
        rabitDist[cmd[i]] = cmd[i+1] # 토끼 별 점프 거리 init

    for _ in range(q-1):
        cmd = list(map(int, input().split()))

        if cmd[0] == 200:
            k, s = cmd[1], cmd[2]
            moved = {}
            for _ in range(k):
                _, y, x, pid = heapq.heappop(rabit[minJump])
                dist = rabitDist[pid]

                npos = [] # 행+열, 행, 열 이 큰 순으로 보관
                for i in range(4):
                    nx = x + dx[i]*(dist % ((m-1)*2))
                    ny = y + dy[i]*(dist % ((n-1)*2))
                    while nx < 0 or nx >= m or ny < 0 or ny >= n:
                        if nx < 0:
                            nx = abs(nx)
                        elif nx >= m:
                            nx = 2*(m-1) - nx
                        elif ny < 0:
                            ny = abs(ny)
                        elif ny >= n:
                            ny = 2*(n-1) - ny

                    npos.append((nx+ny, ny, nx))

                npos.sort(key = lambda x : (-x[0],-x[1],-x[2]))

                # 옮긴 토끼 위치 및 점프 횟수 갱신
                if minJump+1 in rabit:
                    heapq.heappush(rabit[minJump+1],(npos[0][0],npos[0][1],npos[0][2],pid))
                else:
                    rabit[minJump + 1] = [(npos[0][0],npos[0][1],npos[0][2],pid)]
                
                # 최소 점프 횟수 갱신
                if not rabit[minJump]:
                    for i in rabit.keys():
                        if rabit[i]:
                            minJump = i

                # 전체 획득 점수 및 이동한 토끼가 못받은 점수 갱신
                totalScore += (npos[0][0] +2)
                rabitMinusScore[pid] += npos[0][0] +2
                
                # 이동한 토끼 중, 추가 점수 획득을 파악하기 위한 데이터 저장
                moved[pid] = (npos[0][0], npos[0][1], npos[0][2])

            # k번의 턴 종료 후, 추가 점수 부여
            sortedMoved = sorted(moved.items(), key = lambda x : (-x[1][0], -x[1][1], -x[1][2], -x[0]))
            rabitPlusScore[sortedMoved[0][0]] += s

        elif cmd[0] == 300:
            rabitDist[cmd[1]] *= cmd[2]

        elif cmd[0] == 400:
           maxScore = 0
           for jump, queue in rabit.items():
               if not queue:
                   continue
               for _, _, _, pid in queue:
                   maxScore = max(maxScore, totalScore + rabitPlusScore[pid] - rabitMinusScore[pid])

           print(maxScore)