def solution(s):
    answer = ''
    nums = list(map(int, s.split()))
    answer = "%d %d" % (min(nums), max(nums))
    return answer