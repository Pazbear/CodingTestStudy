def solution(s):
    minn, maxn=100000000, -100000000
    for c in s.split(' '):
        temp = int(c)
        if minn > temp:
            minn = temp
        if maxn < temp:
            maxn=temp
    return " ".join([str(minn), str(maxn)])