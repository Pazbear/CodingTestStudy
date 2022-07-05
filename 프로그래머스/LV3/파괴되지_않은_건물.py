def solution(board, skill):
    answer=0
    accum = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for sk in skill:
        tp, r1, c1, r2, c2, degree = sk
        degree *= 1 if tp==2 else -1
        accum[r1][c1]+=degree
        accum[r1][c2+1]-=degree
        accum[r2+1][c1]-=degree
        accum[r2+1][c2+1]+=degree
        #0,0 부터 2,3 까지라면
        #0,0과 3,4 에 degree
        #3,0과 0,4 에 -degree
        # 이후에 가로로 합을 누적해감
        # 가로 후 세로로 합 누적
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            accum[i][j]=accum[i][j]+accum[i][j-1]
    for i in range(1,len(board)):
        for j in range(len(board[0])):
            accum[i][j]=accum[i][j]+accum[i-1][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if accum[i][j]+board[i][j]>0:
                answer+=1
    return answer