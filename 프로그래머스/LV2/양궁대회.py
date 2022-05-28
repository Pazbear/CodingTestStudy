max_gap = 0
answer=[]
def solution(n, info):
    global answer
    dfs(info, [], n, 0)
    if max_gap == 0:
        return [-1]
    answer.sort(key = lambda x : x[::-1], reverse=True)
    return answer[0]

def dfs(info, result,remain, index):
    global max_gap, answer
    if index == 11:
        if remain > 0:
            result[-1]+=remain
        gap = calGap(info, result)
        if max_gap < gap:
            max_gap = gap
            answer = [result]
        elif max_gap == gap:
            answer.append(result)
        return
    if remain > info[index] : #남은게 어피치가 쏜 것보다 많을경우
        dfs(info, result+[info[index]+1], remain-(info[index]+1), index+1)
    dfs(info, result+[0], remain, index+1)
    
def calGap(info, result):
    gap = 0
    for i in range(11):
        if info[i]==0 and result[i] == 0:
            continue
        if info[i]<=result[i]:
            gap+=(10-i)
        else:
            gap-=(10-i)
    return gap