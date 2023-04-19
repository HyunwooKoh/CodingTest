#! solution for baekjoon 1003 prob.
# https://www.acmicpc.net/problem/1003

# 기본이 되는 숫자에 대한 값 설정
# (zeroCount, oneCount)
# num == 0 : (1,0)
# num == 1 : (0,1)
# num == 2 : (1,1)

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length : # 이미 계산한 수인지 확인, 이미 계산한 수라면 바로 출력
        for i in range(length, num+1):
            # 새로 계산
            zero.append(zero[i - 1] + zero[i - 2]) # 해당 수의 0의 개수는 num -2와 num -1의 0의 개수의 합
            one.append(one[i - 1] + one[i - 2]) # 해당 수의 1의 개수는 num -2와 num -1의 0의 개수의 합
    print(str(zero[num]) + ' ' + str(one[num]))

if __name__ == "__main__":
    count = int(input())
    for _ in range(0, count):
        fibonacci(int(input()))