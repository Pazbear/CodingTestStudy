from collections import deque
def solution(n, s, a, b, fares):
    answer = 10000000
    charge=[[10000000 for _ in range(n+1)] for _ in range(3)]
    lines = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for f in fares:
        lines[f[0]][f[1]]=f[2]
        lines[f[1]][f[0]]=f[2]
    arr = [s, a, b]
    for i in range(len(arr)):
        queue=deque()
        queue.append(arr[i])
        charge[i][arr[i]]=0
        while queue:
            temp = queue.popleft()
            for j in range(1,len(lines[temp])):
                if lines[temp][j]>0 and charge[i][j] > charge[i][temp]+lines[temp][j]:
                    charge[i][j]=charge[i][temp]+lines[temp][j]
                    queue.append(j)
    
    for i in range(1,n+1):
        answer = min(answer, charge[0][i]+charge[1][i]+charge[2][i])
            
    return answer