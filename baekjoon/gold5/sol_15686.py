import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    chicken, house = [], []

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 2:
                chicken.append((j,i))
            elif line[j] == 1:
                house.append((j,i))
        mat.append(line)
    
    res = 1e9
    for c in combinations(chicken, m):
        totalDist = 0
        for x1, y1 in house:
            dist = 1e9
            for x2, y2 in c:
                dist = min(dist, abs(x2 - x1) + abs(y2 - y1))
            totalDist += dist
        res = min(res, totalDist)
    print(res)