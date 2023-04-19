from dataclasses import dataclass

@dataclass
class Pos :
    m_x : int
    m_y : int

def strToPos(pos):
    x = y = 0
    if pos[0] == 'A':
        x = 1
    elif pos[0] == 'B':
        x = 2
    elif pos[0] == 'C':
        x = 3
    elif pos[0] == 'D':
        x = 4
    elif pos[0] == 'E':
        x = 5
    elif pos[0] == 'F':
        x = 6
    elif pos[0] == 'G':
        x = 7
    elif pos[0] == 'H':
        x = 8
    y = int(pos[1])
    return Pos(x,y)

def posToStr(pos : Pos):
    res = ""
    if pos.m_x == 1:
        res += 'A'
    elif pos.m_x == 2:
        res += 'B'
    elif pos.m_x == 3:
        res += 'C'
    elif pos.m_x == 4:
        res += 'D'
    elif pos.m_x == 5:
        res += 'E'
    elif pos.m_x == 6:
        res += 'F'
    elif pos.m_x == 7:
        res += 'G'
    elif pos.m_x == 8:
        res += 'H'
    res += str(pos.m_y)
    return res

def directToPos(direct):
    x = y = 0
    if direct == 'R' :
        x = 1
    elif direct == 'L':
        x = -1
    elif direct == 'B':
        y = -1
    elif direct == 'T':
        y = 1
    elif direct == 'RT':
        x = 1
        y = 1
    elif direct == 'LT':
        x = -1
        y = 1
    elif direct == 'RB':
        x = 1
        y = -1
    elif direct == 'LB':
        x = -1
        y = -1
    return Pos(x,y)


if __name__ == "__main__":
    inputs = input().split(' ')
    kingPos = strToPos(inputs[0])
    rockPos = strToPos(inputs[1])
    moveCount = int(inputs[2])

    moveList = []
    for _ in range(moveCount):
        moveList.append(input())

    for i in range(moveCount):
        directPos = directToPos(moveList[i])
        if kingPos.m_x + directPos.m_x > 8 or kingPos.m_x + directPos.m_x < 1:
            continue
        elif kingPos.m_y + directPos.m_y > 8 or kingPos.m_y + directPos.m_y < 1:
            continue
        else:
            if kingPos.m_x + directPos.m_x == rockPos.m_x and kingPos.m_y + directPos.m_y == rockPos.m_y:
                if rockPos.m_x + directPos.m_x > 8 or rockPos.m_x + directPos.m_x < 1:
                    continue
                elif rockPos.m_y + directPos.m_y > 8 or rockPos.m_y + directPos.m_y < 1:
                    continue
                else:
                    kingPos.m_x += directPos.m_x
                    kingPos.m_y += directPos.m_y
                    rockPos.m_x += directPos.m_x
                    rockPos.m_y += directPos.m_y
            else :
                kingPos.m_x += directPos.m_x
                kingPos.m_y += directPos.m_y
    print(posToStr(kingPos))
    print(posToStr(rockPos))