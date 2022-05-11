from collections import deque

def solution(N, road, K):
    answer = 0
    queue = deque()
    queue.append(1)
    village = [1000000 for _ in range(N+1)]
    village[1]=0
    time = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for r in road:
        time[r[0]][r[1]]= min(r[2], time[r[0]][r[1]]) if time[r[0]][r[1]]!=0 else r[2]
        time[r[1]][r[0]]= min(r[2], time[r[1]][r[0]]) if time[r[1]][r[0]]!=0 else r[2]
    while queue:
        temp = queue.popleft()
        for i in range(len(time[temp])):
            if time[temp][i] != 0:
                if village[temp]+time[temp][i] < village[i]:
                    village[i]=village[temp]+time[temp][i]
                    queue.append(i)
                
    for v in village:
        if v <= K:
            answer+=1
    return answer