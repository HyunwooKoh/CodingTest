import sys
import math
input = sys.stdin.readline

def isPrime(num):
    isPrime = True
    if num == 1:
        isPrime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                isPrime = False
                break
    return isPrime

# NOTE: 주석처럼 해당 수 내의 모든 소수를 갖고 조합을 찾고자 하면
# timeout이 발생 함
# 모든 소수의 set이 아닌, 숫자별로 판단하면서 소수인지 확인하는 과정이 더 빠름
if __name__ == "__main__":
    reps = int(input())
    #primes = [2,3,5,7,11]
    #lastNum = 11
    for _ in range(reps):
        num = int(input())
        # if lastNum < num:
        #     for i in range(lastNum+1, num + 1):
        #         if isPrime(i):
        #             primes.append(i)
        #     lastNum = num
        # # if num % 2 == 0 and num // 2 in primes:
        #         print(str(num // 2) + " " + str(num//2))
        # else:
        #     for i in range((len(primes) // 2 + 1), 0, -1):
        #         if (num - primes[i]) in primes:
        #             print(num - primes[i], primes[i])
        #             break
        l, h = num // 2, num // 2
        while l >= 0:
            if isPrime(l) and isPrime(h):
                print(l, h)
                break
            else:
                l -= 1
                h += 1