def solution(n):
    answer=[]
    if n==1:
        return [1]
    tri_snail = [[0 for _ in range(n)] for _ in range(n)]
    dirn = [[1, 0], [0, 1],[-1, -1]]
    cur_dir, cur_num = 0, 1
    cur_pos = [0,0]
    while True:
        tri_snail[cur_pos[0]][cur_pos[1]]=cur_num
        if cur_pos[0]+dirn[cur_dir][0] >=0 and cur_pos[0]+dirn[cur_dir][0] <n and cur_pos[1]+dirn[cur_dir][1] >=0 and cur_pos[1]+dirn[cur_dir][1] <n:
            if tri_snail[cur_pos[0]+dirn[cur_dir][0]][cur_pos[1]+dirn[cur_dir][1]] != 0:
                if tri_snail[cur_pos[0]+dirn[(cur_dir+1)%3][0]][cur_pos[1]+dirn[(cur_dir+1)%3][1]] != 0:
                    break
                else:
                    cur_dir= (cur_dir+1)%3
        else:
            if tri_snail[cur_pos[0]+dirn[(cur_dir+1)%3][0]][cur_pos[1]+dirn[(cur_dir+1)%3][1]] != 0:
                break
            else:
                cur_dir= (cur_dir+1)%3
        cur_pos[0] = cur_pos[0]+dirn[cur_dir][0]
        cur_pos[1] = cur_pos[1]+dirn[cur_dir][1]
        cur_num+=1
    for i in range(1,n+1):
        answer+=tri_snail[i-1][0:i]
    return answer
"""
from itertools import chain
def solution(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))
"""