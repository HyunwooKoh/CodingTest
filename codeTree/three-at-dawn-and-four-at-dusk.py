# ref https://www.codetree.ai/training-field/frequent-problems/problems/three-at-dawn-and-four-at-dusk/
import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [i for i in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]

    res = 1e9
    for comb in combinations(nums, n//2):
        morning = list(comb)
        night = []
        for i in nums:
            if i not in morning:
                night.append(i)
        
        morningRes = 0
        nightRes = 0
        for i in range(len(morning)):
            for j in range(i+1, len(morning)):
                morningRes += p[morning[i]][morning[j]]
                morningRes += p[morning[j]][morning[i]]
        
        for i in range(len(night)):
            for j in range(i+1, len(night)):
                nightRes += p[night[i]][night[j]]
                nightRes += p[night[j]][night[i]]
        res = min(abs(morningRes-nightRes), res)
    print(res)