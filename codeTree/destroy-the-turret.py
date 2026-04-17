# ref https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    mat = []
    lastAttack = {}  # 타워 별 마지막 공격 시간(tern)
    tower = []  # 타워 별 좌표 (x,y)
    towerCnt = 0

    # 타워 데이터 init
    for y in range(n):
        line = list(map(int, input().split()))
        mat.append(line)
        for x in range(m):
            if line[x] != 0:
                towerCnt += 1
                tower.append((x, y))
                lastAttack[(x, y)] = 0

    tern = 0
    while tern < k and towerCnt > 1:
        tern += 1

        # 공격 타워 및 피공격 타워 선정
        tower.sort(key=lambda x: (mat[x[1]][x[0]], -lastAttack[(x[0], x[1])], -sum(x), -x[0]))
        ax, ay = tower[0][0], tower[0][1]
        tx, ty = tower[-1][0], tower[-1][1]

        # 피공격 타워 리스트
        attackedTower = []

        # 레이저 공격
        queue = []
        visited = [[int(n * n)] * m for _ in range(n)]
        queue.append((ax, ay, []))
        visited[ay][ax] = 0
        while queue:
            x, y, history = queue.pop(0)

            # 우/하/좌/상 의 우선순위
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 좌표가 벗어나면, 넘어감
                if nx < 0:
                    nx += m
                elif nx >= m:
                    nx -= m
                elif ny < 0:
                    ny += n
                elif ny >= n:
                    ny -= n

                # 부서진타워는 지나갈 수 없음
                if mat[ny][nx] == 0:
                    continue

                if visited[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    if nx == tx and ny == ty:
                        attackedTower = history.copy() + [(nx, ny)]
                    else:
                        queue.append((nx, ny, history.copy() + [(nx, ny)]))

        # 포탄 공격
        if not attackedTower:
            dx = [1, 1, 1, 0, 0, -1, -1, -1, 0]
            dy = [0, 1, -1, 1, -1, 0, 1, -1, 0]

            for i in range(9):
                nx = tx + dx[i]
                ny = ty + dy[i]

                if nx < 0:
                    nx += m
                if nx >= m:
                    nx -= m
                if ny < 0:
                    ny += n
                if ny >= n:
                    ny -= n

                if nx == ax and ny == ay:
                    continue

                if mat[ny][nx] == 0:
                    continue

                attackedTower.append((nx, ny))

        # 피공격 타워에 대한 공격 수행
        mat[ay][ax] += (n + m)
        damage = mat[ay][ax]
        lastAttack[(ax, ay)] = tern
        remainTower = [(ax, ay)]
        for x, y in tower:
            if (x, y) in attackedTower:
                if x == tx and y == ty:
                    mat[y][x] -= damage
                else:
                    mat[y][x] -= damage // 2

                # 타워 제거됨
                if mat[y][x] <= 0:
                    mat[y][x] = 0
                    towerCnt -= 1
                else:
                    remainTower.append((x, y))
            elif x != ax or y != ay:
                mat[y][x] += 1
                remainTower.append((x, y))
        tower = remainTower.copy()

    res = 0
    for x, y in tower:
        res = max(res, mat[y][x])
    print(res)