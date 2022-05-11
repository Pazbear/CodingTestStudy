def solution(n,a,b):

    return dfs(a, b, 0)
def dfs(a, b, cnt):
    if a == b:
        return cnt
    else:
        return dfs((a+1)//2, (b+1)//2, cnt+1)