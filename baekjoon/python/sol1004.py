from dataclasses import dataclass
import math

@dataclass
class point:
    m_x : int
    m_y : int

@dataclass
class circle:
    m_center : point
    m_r : int


def isInCircle(point : point, circle : circle) :
    if math.sqrt(math.pow(circle.m_center.m_x - point.m_x, 2) + math.pow(circle.m_center.m_y - point.m_y, 2)) < circle.m_r:
        return True
    else:
        return False


if __name__ == "__main__" :
    count = int(input())
    for _ in range (0, count):
        planets = []
        points = input().split(' ')
        start = point(int(points[0]), int(points[1]))
        dest = point(int(points[2]), int(points[3]))
        
        for _ in range(0, int(input())) :
            datas = input().split(' ')
            planets.append(circle(point(int(datas[0]), int(datas[1])), int(datas[2])))
        
        count = 0
        for p in planets:
            startIn = isInCircle(start, p)
            destIn = isInCircle(dest, p)
            if sum([startIn,destIn]) == 1:
                count += 1
        print(count)