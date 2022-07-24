def solution(n):
    return int(''.join(sorted(list(list(str(n))), reverse=True)))