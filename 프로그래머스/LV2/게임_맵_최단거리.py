from collections import deque
direction = [[1,0],[-1,0],[0,1],[0,-1]]
n, m = 0, 0
def isInMap(curx, cury):
    if curx>=0 and curx <n and cury >=0 and cury <m:
        return True
    else:
        return False

def solution(maps):
    global n, m
    n=len(maps)
    m = len(maps[0])
    return bfs(maps)

def bfs(maps):
    queue = deque()
    queue.append([0, 0, 1])
    maps[0][0]=0
    while queue:
        curx, cury,cnt = queue.popleft()
        for i in range(4):
            nextx= curx+direction[i][0]
            nexty= cury+direction[i][1]
            if isInMap(nextx, nexty) and maps[nextx][nexty]==1:
                if nextx==n-1 and nexty==m-1:
                    return cnt+1
                maps[nextx][nexty]=0
                queue.append([nextx, nexty, cnt+1])
    return -1