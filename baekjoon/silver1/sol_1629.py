import sys
input = sys.stdin.readline

# 지수 법칙
#A^m+n = A^m x A^n

# 나머지 분배 법칙
#(AxB)%C = (A%C) *(B%C) % C

def multiply(a, n):
  tmp = multiply(a, n//2)
  if n % 2 == 0:
    return (tmp * tmp) % c
  else:
    return (tmp  * tmp * a) %c
          

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    if b == 1:
      print(a % c)
    else:
       print(multiply(a,b))