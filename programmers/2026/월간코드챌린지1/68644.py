#https://school.programmers.co.kr/learn/courses/30/lessons/68644

import sys
input = sys.stdin.readline

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in answer:
                continue
            else:
                answer.append(numbers[i] + numbers[j])

    return sorted(answer)

if __name__ == "__main__":
    numbers = list(map(int, input().strip().split(',')))
    print(solution(numbers))