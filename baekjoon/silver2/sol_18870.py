import sys
input = sys.stdin.readline

if __name__ == "__main__":
    length = int(input())
    nums = list(map(int, input().split()))
    sortedNums = sorted(list(set(nums)))
    
    res = {}
    for i in range(len(sortedNums)):
        res[sortedNums[i]] = i
    
    for i in nums:
        print(res[i], end = ' ')