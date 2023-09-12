# 영어 끝말잇기
def solution(n, words):
    cnt = 1
    wordDict = {}
    wordDict[words[0]] = 1
    lastChar = words[0][-1]
    
    find = False
    for i in range(1, len(words)):
        cnt += 1
        if words[i] in wordDict or words[i][0] != lastChar:
            find = True
            break        
        else:
            wordDict[words[i]] = 1
            lastChar = words[i][-1]
    print(cnt)
    if find:
        mem = n if cnt % n == 0 else cnt % n
        tryCount = (cnt // n)
        if cnt % n != 0 and mem <= cnt % n:
            tryCount += 1
        return [mem, tryCount]
    else:
        return [0,0]