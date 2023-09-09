def getNum(idx, elements):
    if idx >= len(elements):
        idx = idx - len(elements)
    return elements[idx]

def solution(elements):
    resDict = {}
    for i in range(0, len(elements)):
        nums = []
        for j in range(i, i+len(elements)):
            nums.append(getNum(j, elements))
            resDict[sum(nums)] = 1
        
    return len(resDict.keys())