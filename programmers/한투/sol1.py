def isSmall(ch):
    if 'a' <= ch <= 'z':
        return True
    return False

def isBig(ch):
    if 'A' <= ch <= 'Z':
        return True
    return False

def solution(line):
    lineList = list(line)
    answer = ''
    lastCh = ''
    lastCapital = False

    for i in range(len(lineList)):
        if isSmall(lineList[i]):
            if lastCapital:
                answer += lastCh
            lastCapital = False
        elif isBig(lineList[i]):
            if not lastCapital:
                if i == len(lineList) -1:
                    answer += lineList[i]
                elif isBig(lineList[i+1]):
                    answer += lineList[i]
            lastCapital = True
        lastCh = lineList[i]
    return answer