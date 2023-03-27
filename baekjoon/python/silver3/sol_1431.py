def sumNums(code : str):
    num = 0
    for i in range(len(code)):
        if 48 <= ord(code[i]) and ord(code[i]) <= 57:
            num += int(code[i])
    return num

if __name__ == "__main__":
    count = int(input())
    codes = []
    for _ in range(count):
        codes.append(input())
    
    codes.sort( key = lambda s : (len(s), sumNums(s), s))
    for i in range(len(codes)):
        print(codes[i])