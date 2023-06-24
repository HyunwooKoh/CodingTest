def solution(operations):
    queue = []
    for opToken in operations:
        op, num = opToken.split()
        if op == 'I':
            queue.append(int(num))
        else:
            if len(queue) == 0:
                continue
            elif num == '1':
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
            
    if len(queue) == 0:
        return [0,0]
    else:
        return [max(queue), min(queue)]