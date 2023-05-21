import sys
input = sys.stdin.readline

def star(n):
    if n == 3:
        return ['***','* *','***']

    line = star(n // 3)
    stars = []

    for i in line:
        stars.append(i * 3)
    for i in line:
        stars.append(i + ' '*(n // 3) + i)
    for i in line:
        stars.append(i * 3)

    return stars

if __name__ == "__main__" :
    n = int(input())
    print('\n'.join(star(n)))