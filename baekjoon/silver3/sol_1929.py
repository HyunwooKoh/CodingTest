import sys
input = sys.stdin.readline

def primeNumber(x):
    for i in range(2, int(i**0.5)+1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        if i == 1:
            continue
        
        prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        
        if prime:
            print(i)
        