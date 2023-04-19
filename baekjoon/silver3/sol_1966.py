# 회고
# checkBack 함수 대신 list.index(max(list))를 쓰면 더 짧은 코드로
# 가능하지만, 이는 추가적인 looping이 수반 됨 -> max()와 index() 각기 실행
# 따라서, 해당 함수 사용

import sys
input = sys.stdin.readline

def checkBack(queue : list) :
    max = queue[0]
    index = 0
    for i in range(1, len(queue)):
        if queue[i] > max:
            max = queue[i]
            index = i
    return index


if __name__ == "__main__":
    for _ in range(int(input())):
        num, target = map(int,input().split())
        queue = list(input().split())
        count = 1
        while True:
            check = checkBack(queue)
            target -= check
                
            if target == 0:
                print(count)
                break
            elif target < 0: 
                target += (len(queue))


            for i in range(check):
                queue.append(queue.pop(0))
            queue.pop(0)
            target -= 1
            count += 1
