def solution(n, s):
    answer=[]
    if s<n:
        return [-1]
    val = s//n
    mod = s%n
    for _ in range(n-mod):
        answer.append(val)
    for _ in range(mod):
        answer.append(val+1)
    return answer