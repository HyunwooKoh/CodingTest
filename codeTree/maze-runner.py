# ref https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def findSqure():
    for size in range(2, n + 1):
        for y1 in range(n - size + 1):
            for x1 in range(n - size + 1):
                x2, y2 = x1 + size - 1, y1 + size - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵
                if not (x1 <= ex <= x2 and y1 <= ey <= y2):
                    continue

                # 한 명 이상의 참가자가 해당 정사각형 안에 있다면 확정
                for rx, ry in runner:
                    if x1 <= rx <= x2 and y1 <= ry <= y2:
                        return size, x1, y1


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    runner = []
    for _ in range(m):
        y, x = map(int, input().split())
        runner.append((x - 1, y - 1))
    ex, ey = map(int, input().split())
    ex, ey = ex - 1, ey - 1
    time, move = 0, 0

    while time < k and runner:
        # 이동
        changedrunner = []
        for px, py in runner:
            dist = abs(px - ex) + abs(py - ey)
            minDist = dist
            minPos = ()

            for i in range(4):
                nx = px + dx[i]
                ny = py + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if mat[ny][nx] != 0:
                    continue

                nDist = abs(nx - ex) + abs(ny - ey)
                # 최단거리가 감소하는 곳으로만 이동
                if dist <= nDist:
                    continue
                # 상/하가 우선되므로, 찾는 즉시 종료
                if nDist < minDist:
                    minDist = nDist
                    minPos = (nx, ny)
                    break

            if minDist == dist:  # 움직일 수 없는 경우
                changedrunner.append((px,py))
            else:
                move += 1
                if minPos[0] == ex and minPos[1] == ey:
                    # 출구로 나가는 경우 해당 탐험가 제거
                    continue
                else:
                    changedrunner.append(minPos)

        del runner
        runner = changedrunner.copy()
        if not runner:
            break

        # 정사각형 돌리기
        # 이 떄, 사람 및 출구의 좌표도 바뀌어야 함.
        length, tlx, tly = findSqure()
        targetMat = []
        for y in range(tly, tly + length):
            targetMat.append(mat[y][tlx: tlx + length].copy())

        changedrunner = []
        newEx, newEy = -1, -1
        for y in range(length):
            for x in range(length):
                orgx, orgy = tlx + x, tly + y
                nx, ny = tlx + (length - 1) - y, tly + x

                mat[ny][nx] = targetMat[y][x]
                if targetMat[y][x] > 0:
                    mat[ny][nx] -= 1

                if orgx == ex and orgy == ey:
                    newEx, newEy = nx, ny
                elif (orgx, orgy) in runner:
                    runner.remove((orgx, orgy))
                    changedrunner.append((nx, ny))

        runner += changedrunner.copy()
        ex, ey = newEx, newEy
        time += 1

    print(move)
    print(str(ex + 1) + " " + str(ey + 1))