def solution(board):
    answer = 1234
    len_r= min(len(board), len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i==0 or j==0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1], min(board[i][j-1],board[i-1][j]))+1
    answer=0
    for i in range(len(board)):
        answer = max(answer, max(board[i]))
    return answer **2