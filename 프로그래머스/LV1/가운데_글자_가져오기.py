def solution(s):
    start = int((len(s)/2 - 0.5))
    end = start+(2 if len(s)%2==0 else 1)
    return s[start: end]