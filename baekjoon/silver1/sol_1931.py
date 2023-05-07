import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    meets = []
    for _ in range(num):
        meets.append(list(map(int, input().split())))
    
    meets.sort(key= lambda x : (x[1], x[0]))

    count = 0
    last = 0
    for start, end in meets:
        if last <= start:
            count += 1
            last = end
    print(count)