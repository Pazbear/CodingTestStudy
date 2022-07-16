def solution(n):
    answer = 0
    return int(_10toReverse3(n), 3)

def _10toReverse3(n):
    res=""
    while n>0:
        div, mod = divmod(n, 3)
        n=div
        res+=str(mod)
    return res