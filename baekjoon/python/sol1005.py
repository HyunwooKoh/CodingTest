def calcMoveCount(size, pos):
    if size == 1 or pos == 1:
        return 0
    if pos <= (size + 1)/ 2 :
        return -(pos - 1)
    else :
        return size + 1 - pos

if __name__ == "__main__":
    inputString = input().split(' ')
    listSize = int(inputString[0])
    pickCount = int(inputString[1])
    list = input().split(' ')
    list = [int(i) for i in list]
    moveCount = 0
    for i in range(0, len(list)):
        res = calcMoveCount(listSize, list[0])
        moveCount += abs(res)
        for j in range(0, len(list)) :
            list[j] = list[j] + res - 1
            if list[j] <= 0 :
                list[j] = list[j] + listSize 
            elif list[j] > listSize :
                list[j] = list[j] - listSize
        list.pop(0)
        listSize -= 1
    print(moveCount)