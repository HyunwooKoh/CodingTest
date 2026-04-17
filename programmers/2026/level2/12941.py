import sys

input = sys.stdin.readline

def solution(A,B):
    answer_a = 0
    answer_b = 0

    sort_a = sorted(A,reverse=True)
    sort_b = sorted(B)

    for i in range(len(sort_a)):
        answer_a += sort_a[i] * sort_b[i]

    sort_a = sorted(A)
    sort_b = sorted(B,reverse=True)

    for i in range(len(sort_a)):
        answer_b += sort_a[i] * sort_b[i]

    
    return min(answer_a, answer_b)

    

if __name__ == "__main__":
    list_a = list(map(int,input().strip().split(',')))
    list_b = list(map(int,input().strip().split(',')))

    print(solution(list_a, list_b))