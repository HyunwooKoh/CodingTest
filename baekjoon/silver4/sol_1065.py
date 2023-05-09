import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = int(input())
    count = 0
    for i in range(1, num+1):
        nums = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif nums[0]-nums[1] == nums[1]-nums[2]:
            count += 1
    print(count)