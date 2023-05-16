import sys
input = sys.stdin.readline

if __name__ == "__main__":
    _ = int(input())
    card = map(int, input().split())
    _ = int(input())
    find = map(int, input().split())

    hash = {}
    for c in card:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    
    print(' '.join(str(hash[i]) if i in hash else '0' for i in find))