if __name__ == "__main__":
    sound = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    m,n = map(int, input().split())
    line = list(input().split())
    code = list(input().split())
    minP = maxP = 0
    for c in code:
        if c in line:
            continue
        else:
            pratt = 11
            for l in line:
                move = sound.index(c) - sound.index(l)
                if move < 0 :
                    move += 12
                if move < pratt:
                    pratt = move
            print(pratt)
            if minP == maxP == 0 :
                minP = maxP = pratt
            elif pratt > maxP:
                maxP = pratt
            elif minP == 0 or minP > pratt:
                minP = pratt
            
    if minP == maxP == 0:
        print(0)
    elif minP == maxP:
        minP == 0
        print(maxP - minP + 1)
    else:        
        print(maxP - minP + 1)