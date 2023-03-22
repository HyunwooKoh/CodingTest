if __name__ == "__main__":
    name = input()
    alphas = {}
    oddChar = ''
    for i in range(len(name)):
        if name[i] in alphas:
            alphas[name[i]] += 1
        else:
            alphas[name[i]] = 1

    alphas = sorted(alphas.items())
    front = ''
    for i in range(len(alphas)):
        key,val = alphas[i]
        if val % 2 != 0:
            if oddChar == '':
                oddChar = key
                for _ in range(val // 2):
                    front += key
            else:
                print("I'm Sorry Hansoo")
                exit(0)
        else :
            for _ in range(val // 2):
                front += key
    back = list(front)
    back.reverse()
    
    front += oddChar
    front += ''.join(back)
    print(front)