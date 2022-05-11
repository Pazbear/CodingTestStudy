"""
블로그 참고

error: 
한번에 지우고 이동시켜야 했는데 한번 지울때마다 이동시켜서 몇몇 테스트케이스에 불통함.
"""
def solution(m, n, board): 
    answer = 0 
    # 지울거 찾기 
    def find(board): 
        target = set() 
        for i in range(m-1): 
            for j in range(n-1): 
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]: 
                    target.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)}) 
        return target 
    def remove(target, board): 
        board = [list(row) for row in board] 
        for loc in target: 
            i, j = loc 
            board[i][j] = '' 
        return board 
    # 이동하기 
    def move(board): 
        cnt = 0 
        for i in range(m-1): 
            for j in range(n): 
                if board[i][j] and not board[i+1][j]: 
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j] 
                    cnt += 1 
        return cnt, board 

    while 1: 
        target = find(board) 
        answer += len(target) 
        board = remove(target, board) 
        cnt = 1 
        while cnt: 
            cnt, board = move(board) 
        if not cnt and not len(target): 
            break 
    return answer