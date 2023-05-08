import sys
input = sys.stdin.readline

def mvTower(num, start, end) :
    if num == 1 :
        print(start, end)
        return
       
    mvTower(num-1, start, 6-start-end)
    print(start, end)
    mvTower(num-1, 6-start-end, end)

if __name__ == "__main__":
    num = int(input())
    count = 1
    for i in range(num - 1):
        count = count * 2 + 1
    print(count)
    mvTower(num, 1, 3)