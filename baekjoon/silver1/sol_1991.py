import sys
input = sys.stdin.readline

def travel(p, preOrder, inOrder, postOrder):
    preOrder.append(p)
    if node[p][0] != '.':
        travel(node[p][0], preOrder, inOrder, postOrder)
    inOrder.append(p)
    if node[p][1] != '.':
        travel(node[p][1], preOrder, inOrder, postOrder)
    postOrder.append(p)
    

if __name__ == "__main__":
    num = int(input())
    node = {}
    for _ in range(num):
        root, left, right = map(str, input().split())
        node[root] = [left, right]
    
    preOrder = []
    inOrder = []
    postOrder = []
    travel('A', preOrder, inOrder, postOrder)
    print(''.join(preOrder))
    print(''.join(inOrder))
    print(''.join(postOrder))