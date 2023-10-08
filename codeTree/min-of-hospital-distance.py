# ref https://www.codetree.ai/training-field/frequent-problems/problems/min-of-hospital-distance
import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    hospital = []
    human = []
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(n):
            if line[x] == 1: # 사람인 경우
                human.append((x,y))
            elif line[x] == 2: # 병원인 경우에 병원의 좌표 기록 및 빈칸화
                hospital.append((x,y))
                line[x] = 0
    
    res = 1e9
    for comb in combinations(hospital, m): # 정해진 개수만큼의 병원 선택
        tmpRes = 0
        for humX, humY in human: # 사람 별로 병원 거리 최솟값 계산
            humanRes = 1e9
            for hosX, hosY in comb: # 병원 별 거리 계산
                dist = abs(humX - hosX) + abs(humY - hosY)
                humanRes = min(humanRes, dist)
            tmpRes += humanRes
        res = min(res, tmpRes)
    
    print(res)