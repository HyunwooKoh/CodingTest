import sys
input = sys.stdin.readline

# rotate
# gear[i] = gear[i][1:] + gear[i][0] -> 북이 끝으로 (반시계)
# gear[i] = gear[i][:-1] + gear[i][:6] -> 끝이 북으로 (시계)
# 왼쪽 index : 6, 오른쪽 index : 2

    
if __name__ == "__main__":
    gear = [list(map(int, input().strip())) for _ in range(4)] 
    k = int(input())
    rotate = []
    for _ in range(k):
        rotate.append(list(map(int, input().split())))

    for i in range(k):  
        target, way = rotate[i][0] -1, rotate[i][1]
        turnTarget = [(target,way)]
        
        # find left side
        lastMg = gear[target][6]
        lastWay = way
        for j in range(target-1, -1, -1):
            if gear[j][2] != lastMg:
                lastMg = gear[j][6]
                lastWay *= -1
                turnTarget.append((j,lastWay))
            else:
                break
        
        # find right side
        lastMg = gear[target][2]
        lastWay = way
        for j in range(target+1, len(gear)):
            if gear[j][6] != lastMg:
                lastMg = gear[j][2]
                lastWay *= -1
                turnTarget.append((j,lastWay))
            else:
                break

        for i in range(len(turnTarget)):
            target, way = turnTarget[i]
            if way == 1: # turn right
                gear[target] = [gear[target][7]] + gear[target][:-1]
            else: # turn left
                gear[target] = gear[target][1:] + [gear[target][0]]
    
    res = 0
    for i in range(4):
        res += 2**i if gear[i][0] == 1 else 0
    print(res)