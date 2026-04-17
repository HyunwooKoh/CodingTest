# ref https://www.codetree.ai/training-field/frequent-problems/problems/santa-gift-factory
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    q = int(input())
    cmd = list(map(int, input().split()))
    N = cmd[1]
    M = cmd[2]

    belt = [[] for _ in range(M)]
    belt_available = [True] * M
    prev_belt = [i-1 for i in range(M)]
    next_belt = [i+1 for i in range(M)]
    prev_belt[0] = M-1
    next_belt[M-1] = 0

    box_id_to_idx = {}
    box_belt_index = [-1] * N
    box_belt_num = [-1] * N
    box_weight = [-1] * N

    beltCnt, beltIdx, cnt  = 0, 0, 0
    for i in range(N):
        boxId, boxWeight = cmd[3+i]-1, cmd[3+N+i]
        box_id_to_idx[boxId] = cnt
        box_belt_index[cnt] = beltIdx
        box_belt_num[cnt] = beltCnt
        box_weight[cnt] = boxWeight
        belt[beltCnt].append(boxId)

        beltIdx += 1
        cnt += 1
        if beltIdx == N // M:
            beltCnt += 1
            beltIdx = 0

    for _ in range(q-1):

        cmd = list(map(int, input().split()))

        if cmd[0] == 200:
            weight = cmd[1]
            # 각 벨트를 돌며, 처음에 있는 것이 weight보다 같거나 작은지 확인
            res = 0
            for i in range(M):
                if box_weight[box_id_to_idx[belt[i][0]]] <= weight: # 같거나 작으면 박스를 빼고, 해당 레일의 모든 상자들에 대해 index -1
                    target = belt[i].pop(0)
                    index = box_id_to_idx[target]

                    del box_id_to_idx[target] # 첫번째 상자 제거 및 인덱스 매핑 제거

                    res += box_weight[index]
                    for j in belt[i]:
                        index = box_id_to_idx[j]
                        box_belt_index[index] -= 1

                else:
                    # 크다면, 해당 상자를 위에다가 둠
                    tmp = belt[i].pop(0)
                    for j in belt[i]:
                        index = box_id_to_idx[j]
                        box_belt_index[index] -= 1
                    box_belt_index[box_id_to_idx[tmp]] = len(belt[i])
                    belt[i].append(tmp)
            print(res)

        elif cmd[0] == 300:
            rid = cmd[1]-1

            # 상자가 벨트 내에 없는 경우
            if not rid in box_id_to_idx:
                print(-1)
            else:
                targetBelt = box_belt_num[box_id_to_idx[rid]]
                targetIndex = box_belt_index[box_id_to_idx[rid]]

                # 벨트에서 타깃 제거
                belt[targetBelt].pop(targetIndex)
                del box_id_to_idx[rid]

                # 남은 상자에 대한 인덱스 수정
                for i in range(targetIndex, len(belt[targetBelt])):
                    index = box_id_to_idx[belt[targetBelt][i]]
                    box_belt_index[index] -= 1

                print(rid+1)

        elif cmd[0] == 400:
            fid = cmd[1]-1

            if not fid in box_id_to_idx:
                print(-1)
            else:
                targetBelt = box_belt_num[box_id_to_idx[fid]]
                targetIndex = box_belt_index[box_id_to_idx[fid]]

                belt[targetBelt] = belt[targetBelt][targetIndex:] + belt[targetBelt][:targetIndex]

                # 옮겨진 박스들에 대한 index 갱신 O(n)
                for i in range(len(belt[targetBelt])):
                    index = box_id_to_idx[belt[targetBelt][i]]
                    box_belt_index[index] = i

                print(targetBelt+1)

        elif cmd[0] == 500:
            bNum = cmd[1]-1

            # 이미 고장나 있으면 -1
            if not belt_available[bNum]:
                print(-1)
            else:
                # 이전 벨트와 다음 벨트의 next를 연결
                prevBelt = prev_belt[bNum]
                nextBelt = next_belt[bNum]
                next_belt[prevBelt] = nextBelt
                prev_belt[nextBelt] = prevBelt

                # 벨트 내의 물건을 Next로 이동
                startIndex = len(belt[nextBelt])
                for i in range(len(belt[bNum])):
                    index = box_id_to_idx[belt[bNum][i]]
                    box_belt_num[index] = nextBelt
                    box_belt_index[index] = startIndex + i

                belt_available[bNum] = False
                belt[bNum] = []
                print(bNum+1)