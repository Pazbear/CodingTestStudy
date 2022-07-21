def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdecimal():
            return True
    return False