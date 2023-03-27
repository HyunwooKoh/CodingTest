if __name__ == "__main__":
    tryCount = int(input())
    def getLen(p1,p2):
        return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

    for _ in range(tryCount):
        square=[]
        for _ in range(4):
            x, y=map(int,input().split())
            square.append([x, y])

        square=sorted(square)
        center = 0
        for p in square:
            if p == [0,0]:
                center += 1
        if center == 4:
            print(0)
        elif getLen(square[0], square[1]) == getLen(square[0], square[2]) == getLen(square[1], square[3]) and getLen(square[1],square[2]) == getLen(square[0], square[3]):
            print(1)
        else:
            print(0)