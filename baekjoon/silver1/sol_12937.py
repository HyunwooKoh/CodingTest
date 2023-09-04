# 짝지어 제거하기

def solution(s):
# 문자열 풀이
#     reString = s[0]
#     lastIdx = 0
#     for idx in range(1,len(s)):
#         if len(reString) == 0:
#             reString += s[idx]
#             lastIdx = 0
#         elif reString[lastIdx] != s[idx]:
#             reString += s[idx]
#             lastIdx += 1
#         else: 
#             reString = reString[:-1]
#             lastIdx -= 1    
    
#     return 1 if len(reString) == 0 else 0
   
# STACK 풀이
    stack = []
    for ch in s:
        if not stack :
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 0 if stack else 1