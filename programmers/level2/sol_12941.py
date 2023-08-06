# 최솟값 만들기
def solution(A,B):
    # sol1
    if False:
        A.sort()
        B.sort()
        aReverse = sorted(A, reverse = True)
        bReverse = sorted(B, reverse = True)
        
        res1 = 0
        for i in range(len(A)):
            res1 += A[i] * bReverse[i]
        
        res2 = 0
        for i in range(len(A)):
            res2 += aReverse[i] * B[i]
            
        return min(res1,res2)
    
    # sol2
    res = 0
    if max(A) > max(B):
        aReverse = sorted(A, reverse = True)
        B.sort()
        for i in range(len(A)):
            res += aReverse[i] * B[i]
    else:
        bReverse = sorted(B, reverse = True)
        A.sort()
        for i in range(len(A)):
            res += bReverse[i] * A[i]
    return res