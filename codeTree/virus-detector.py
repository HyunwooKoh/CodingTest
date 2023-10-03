# # 삼성 SW역량 테스트 기출문제 - 바이러스 검사
# ref https://www.codetree.ai/training-field/frequent-problems/problems/virus-detector
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    restraunt = list(map(int, input().split()))
    a, b = map(int, input().split())

    res = n
    for r in restraunt:
        if r-a > 0 :
            res += (r-a)//b + 1 if (r-a) % b > 0 else (r-a)//b 
    
    print(res)