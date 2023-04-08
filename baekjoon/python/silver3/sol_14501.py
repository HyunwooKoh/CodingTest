import sys
input = sys.stdin.readline

def func(cases : list, pays : list, choose : list):
    lastJob = -1
    if len(choose) > 0 :
        lastJob = choose[len(choose) - 1]
    day = lastJob + cases[lastJob][0] if lastJob != -1 else 0
    
    plus = False
    for i in range(day, len(cases)):
        if i + cases[i][0] <= len(cases):
            plus = True
            choose.append(i)
            func(cases, pays, choose)
            choose.pop()
    if day == len(cases) or not plus:
        pay = 0
        for i in choose:
            pay += cases[i][1]
        pays.append(pay)

if __name__ == "__main__":
    num = int(input())
    cases = []
    pays = []
    for _ in range(num):
        day, pay = map(int, input().split())
        cases.append([day, pay])
    func(cases, pays, [])
    print(max(pays))