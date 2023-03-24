if __name__ == "__main__":
    n = int(input())
    way = input()
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    mMap = [['#' for _ in range(101)] for _ in range(101)]
    
    d = 0
    x = y = 50
    minX = maxX = minY = maxY = 50
    mMap[y][x] = '.'
    for w in way:
        if w == 'L':
            d = (d + 3) % 4
        elif w == 'R':
            d = (d + 1) % 4
        else:
            x, y = x + dx[d], y + dy[d]
            mMap[y][x] = '.'
            match d:
                case 0:
                    maxY = max(y, maxY)
                case 1:
                    minX = min(x, minX)
                case 2:
                    minY = min(y, minY)
                case 3:
                    maxX = max(x, maxX)
    
    for i in range(minY, maxY + 1):
        line = ''
        for j in range(minX, maxX + 1):
            line += mMap[i][j]
        print(line)