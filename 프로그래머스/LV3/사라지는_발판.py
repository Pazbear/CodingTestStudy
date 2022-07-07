direction = [[0,1],[0,-1],[1,0],[-1,0]]
n, m =0, 0
visited = [[0]*5 for _ in range(5)]
block = [[0]*5 for _ in range(5)]
def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            block[i][j] = board[i][j]
    return dfs(aloc, bloc)


def dfs(curloc, oploc):
    global visited, block
    if visited[curloc[0]][curloc[1]]:
        return 0
    ret =0
    for dir in direction:
        nextloc = [curloc[0]+dir[0], curloc[1]+dir[1]]
        if nextloc[0]>=0 and nextloc[0]<n and nextloc[1]>=0 and nextloc[1]<m:
            if visited[nextloc[0]][nextloc[1]] == 0 and block[nextloc[0]][nextloc[1]]==1:
                visited[curloc[0]][curloc[1]]=1
                val = dfs(oploc, nextloc)+1
                visited[curloc[0]][curloc[1]]=0
                
                if ret %2==0 and val%2 ==1:
                    ret = val
                elif ret %2 == 0 and val%2 == 0: 
                    ret = max(ret, val)
                elif ret%2==1 and val%2==1:
                    ret = min(ret, val)
    return ret