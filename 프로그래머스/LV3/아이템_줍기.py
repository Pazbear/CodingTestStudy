from collections import deque
#사각형 안에 벽을 만들기 위해 사각형의 크기를 두배로 만듬(1*n, n*1은 벽을 구분할 수 있는 좌표를 만들 수 없으므로)
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    direction = [[0, 1],[0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append([characterX*2,characterY*2, 0])
    stopby = [[0 for _ in range(101)] for _ in range(101)]
    stopby[characterX*2][characterY*2]=1
    board = [[0 for _ in range(101)] for _ in range(101)]
    for rec in rectangle:
        for i in range(rec[0]*2, rec[2]*2+1):
            for j in range(rec[1]*2, rec[3]*2+1):
                if board[i][j]!=2 and (i==rec[0]*2 or i == rec[2]*2 or j==rec[1]*2 or j == rec[3]*2):
                    board[i][j]=1
                else:
                    board[i][j]=2
    while queue:
        tx, ty, distance = queue.popleft()
        stopby[tx][ty]=1
        if tx == itemX*2 and ty == itemY*2:
            return distance //2
        for d in direction:
            if tx+d[0]>=0 and tx+d[0]<101 and ty+d[1]>=0 and ty+d[1]<101 and board[tx+d[0]][ty+d[1]]==1 and  stopby[tx+d[0]][ty+d[1]]==0:
                queue.append([tx+d[0], ty+d[1], distance+1])
    return answer