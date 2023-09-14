# 삼성 SW역량 테스트 기출문제 - 조삼모사
# ref https://www.codetree.ai/training-field/frequent-problems/problems/three-at-dawn-and-four-at-dusk/

import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [i for i in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]

    for comb in combinations(nums, n//2):
        # comb -> 아침
        # not comb -> 저녁
        # 강도 개산 함수 구현
        # 차이 값 확인 후 갱신