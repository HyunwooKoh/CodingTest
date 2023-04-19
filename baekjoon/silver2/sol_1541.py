import sys
input = sys.stdin.readline

if __name__ == "__main__":
    mt = input().split('-')
    nums = []
    for t in mt:
        tokens = t.split('+')
        num = sum([int(num) for num in tokens])
        nums.append(num)
    res = nums[0]
    for i in range(1, len(nums)):
        res -= nums[i]
    print(res)