"""
코드가 매우 비효율적.
"""
def solution(dirs):
    answer = 0
    curr= [0,0]
    move=[[0,-1],[0,1],[1,1],[1,-1]]
    visited = {}
    for dir in dirs:
        comm = 0
        if dir == 'U':
            if curr[0]-1 <-5:
                continue
            comm=0
        elif dir == 'D':
            if curr[0]+1 >5:
                continue
            comm=1
        elif dir == 'R':
            if curr[1]+1 >5:
                continue
            comm=2
        elif dir == 'L':
            if curr[1]-1 <-5:
                continue
            comm=3
        next = [curr[0]+move[comm][1], curr[1]] if move[comm][0]==0 else [curr[0], curr[1]+move[comm][1]]
        temp = (tuple(curr), tuple(next)) if curr[0] < next[0] or (curr[0]==next[0] and curr[1]< next[1]) else (tuple(next), tuple(curr))
        curr = next
        if temp not in visited:
            visited[temp]=0
            answer+=1
    return answer