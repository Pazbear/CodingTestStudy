def solution(board, moves):
    answer = 0
    basket=[]
    tboard = [[] for _ in range(len(board))]
    for i in range(len(board[0])-1,-1,-1):
        for j in range(len(board)-1,-1,-1):
            if board[j][i]!=0:
                tboard[i].append(board[j][i])

    for move in moves:
        if tboard[move-1]:
            temp = tboard[move-1].pop()
            if basket and basket[-1]==temp:
                basket.pop()
                answer+=2
            else:
                basket.append(temp)
    return answer