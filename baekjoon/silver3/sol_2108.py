import sys
input = sys.stdin.readline

def average(nums : list):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)

def center(nums : list):
    nums.sort()
    if len(nums) % 2 == 0 :
        return nums[len(nums) // 2] + nums[(len(nums) // 2)+ 1] / 2
    else:
        return nums[len(nums) // 2]
    
def frequency(nums : list):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    maxValue = max(freq.values())
    maxFreq = []
    for key in freq.keys():
        if freq[key] == maxValue:
            maxFreq.append(key)
    
    if len(maxFreq) > 1:
        maxFreq.sort()
        return maxFreq[1]
    else:
        return maxFreq[0]

def calcRange(nums : list):
    return max(nums) - min(nums) 

if __name__ == "__main__":
    count = int(input())
    nums = [int(input()) for _ in range(count)]
    print(round(average(nums)))
    print(center(nums))
    print(frequency(nums))
    print(calcRange(nums))