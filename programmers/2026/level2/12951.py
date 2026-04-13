def solution(s):
    slist = s.split(' ')
    result = []
    for i in range(len(slist)):
        slist[i] = slist[i][:1].upper() + slist[i][1:].lower()
        result = ' '.join(slist)
    return result