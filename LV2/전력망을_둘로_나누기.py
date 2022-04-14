from collections import deque
def solution(n, wires):
    answer=1000000
    line = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for wire in wires:
        line[wire[0]][wire[1]]=1
        line[wire[1]][wire[0]]=1
    for wire in wires:
        line[wire[0]][wire[1]]=0
        line[wire[1]][wire[0]]=0
        answer = min(answer, bfs(n, line))
        line[wire[0]][wire[1]]=1
        line[wire[1]][wire[0]]=1
    return answer
    
def bfs(n, line):
    stopby = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        queue = deque()
        cnt=0
        if stopby[i] == 0:
            queue.append(i)
            while queue:
                cnt+=1
                temp = queue.popleft()
                stopby[temp]=1
                for j in range(1, n+1):
                    if line[temp][j] == 1 and stopby[j]==0:
                        queue.append(j)
            return abs(n-2 * cnt)