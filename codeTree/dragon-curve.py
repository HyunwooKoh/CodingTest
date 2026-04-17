# ref https://www.codetree.ai/training-field/frequent-problems/problems/dragon-curve
import sys
input = sys.stdin.readline

GRID_SIZE = 100

# 변수 선언 및 입력
n = int(input())

# 현재 드래곤 커브를 이루고 있는 점들의 위치를 나타내는 배열입니다.
dragon_point = [
    [False for _ in range(GRID_SIZE + 1)]
    for _ in range(GRID_SIZE + 1)
]

# 현재 세대에서 새롭게 그려지는 드래곤 커브 점들을 나타내는 배열입니다.
new_dragon_point = [
    [False for _ in range(GRID_SIZE + 1)]
    for _ in range(GRID_SIZE + 1)
]

# 최종적으로 그려지는 드래곤 커브들의 점들을 나타내는 배열입니다.
paper = [
    [False for _ in range(GRID_SIZE + 1)]
    for _ in range(GRID_SIZE + 1)
]


# (x, y)점을 (center_x, center_y)를 기준으로 
# 시계방향으로 90' 회전변환 했을 떄의 좌표값을 반환합니다.
def rotate(x, y, center_x, center_y):
    return (y - center_y + center_x, center_x - x + center_y)


# (center_x, center_y) 위치를 기준으로
# dragon point 점들을 전부 시계 방향으로
# 90' 회전변환 시켜 해당 위치에 점을 추가합니다.
def simulate(center_x, center_y):
    # 새로운 dragon point 값을 초기화 합니다.
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            new_dragon_point[i][j] = False
            
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if dragon_point[i][j]:
                next_x, next_y = rotate(i, j, center_x, center_y)
                new_dragon_point[next_x][next_y] = True
    
    # 새로운 dragon point들을 현재 dragon point에 추가합니다.
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if new_dragon_point[i][j]:
                dragon_point[i][j] = True


def draw_dragon_curve(x, y, d, g):
    # dragon_point 값을 초기화 합니다.
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            dragon_point[i][j] = False
            
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    
    # 0차 드래곤 커브를 만듭니다.
    start_x, start_y = x, y
    end_x, end_y = x + dxs[d], y + dys[d]
    
    dragon_point[start_x][start_y] = True
    dragon_point[end_x][end_y] = True
    
    # g번에 걸쳐 드래곤 커브를 확장시킵니다.
    for _ in range(g):
        # 드래곤 커브를 확장시킵니다.
        simulate(end_x, end_y)
        
        # 현재 드래곤 커브의 마지막 위치를 갱신합니다.
        end_x, end_y = rotate(start_x, start_y, end_x, end_y)
    
    # g차 드래곤 커브 점들을 paper에 전부 표시해줍니다.
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if dragon_point[i][j]:
                paper[i][j] = True


for _ in range(n):
    x, y, d, g = tuple(map(int, input().split()))
    draw_dragon_curve(x, y, d, g)

# 4개의 꼭지점이 전부 드래곤 커브의
# 일부인 칸의 개수를 셉니다.
ans = sum([
    1
    for i in range(GRID_SIZE)
    for j in range(GRID_SIZE)
    if paper[i][j] and paper[i][j + 1] 
    and paper[i + 1][j] and paper[i + 1][j + 1]
])

# 출력:
print(ans)