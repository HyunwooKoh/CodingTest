# ref https://www.codetree.ai/training-field/frequent-problems/problems/codetree-judgers
import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    q = int(input())
    domainHistory = {} # 도메인 : [시작시간, 종료시간]
    waitingDomain = {} # Domain : [도메인 별 대기 작업 : (우선순위, 도착시간, url)]
    waitingUrl = [] # 대기중인 URL
    processingDomain = [] # 체점중인 도메인
    
    # 첫 번째 라인
    cmd = list(map(str, input().split()))
    
    # 체점기 초기화
    n = int(cmd[1])
    judgers = [[False, "", 0] for _ in range(n)] # 체점여부, 도메인, 시작시간
    waitingJudjer = [i for i in range(n)]
    
    # 첫 번째 입력 작업에 따른 대기상태 Init
    waitingDomain[cmd[2][:cmd[2].index('/')]] = [(1, 0, cmd[2])]
    waitingUrl.append(cmd[2])
    waitingQueueLen = 1

    for _ in range(q-1):
        cmd = list(map(str, input().split()))
        
        if cmd[0] == "200":
            t, p, url, domain = int(cmd[1]), int(cmd[2]), cmd[3], cmd[3][:cmd[3].index('/')]
            
            if url in waitingUrl:
                continue
            else:
                waitingQueueLen += 1
                waitingUrl.append(url)
                if domain in waitingDomain:
                    heapq.heappush(waitingDomain[domain], (p, t, url))
                else:
                    waitingDomain[domain] = [(p, t, url)]

        elif cmd[0] == "300" and waitingJudjer:
            t = int(cmd[1])
            targetDomain = ""
            minP, minT = int(1e6), int(1e7)
            
            for domain, queue in waitingDomain.items():
                
                # 해당 도메인의 queue가 비어있는 경우
                if not queue:
                    continue
                
                # 현재 체점중인 도메인은 생략
                if domain in processingDomain: 
                    continue
                # 부적절한 요청 생략
                elif domain in domainHistory:
                    if t < domainHistory[domain][0] + 3*(domainHistory[domain][1] - domainHistory[domain][0]):
                        continue
                
                # 최우선 작업 업데이트
                if queue[0][0] < minP or (queue[0][0] == minP and queue[0][1] < minT):
                    targetDomain = domain
                    minP = queue[0][0]
                    minT = queue[0][1]

            if targetDomain != "":
                judgerId = heapq.heappop(waitingJudjer)
                _, _, url = heapq.heappop(waitingDomain[targetDomain])
                waitingQueueLen -= 1
                processingDomain.append(targetDomain)
                waitingUrl.remove(url)
                judgers[judgerId] = [True, targetDomain, t]


        elif cmd[0] == "400":
            t, id = int(cmd[1]), int(cmd[2]) - 1
            if not judgers[id][0]:
                continue
            else:
                # 작업 종료
                processingDomain.remove(judgers[id][1])
                domainHistory[judgers[id][1]] = [judgers[id][2], t]
                judgers[id] = [False, "", 0]
                heapq.heappush(waitingJudjer, id)
                
        elif cmd[0] == "500":
            print(waitingQueueLen)