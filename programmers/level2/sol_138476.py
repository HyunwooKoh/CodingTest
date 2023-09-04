#귤 고르기
def solution(k, tangerine):
    ans = 0
    tanDict = {}
    tan = []
    for t in tangerine:
        if t in tanDict:
            tanDict[t] += 1
        else:
            tanDict[t] = 1
            tan.append(t)
    tan.sort(key = lambda x : tanDict[x], reverse = True)
    
    for t in tan:
        ans += 1
        k -= tanDict[t]
        if k <= 0:
            break
    return ans