"""
답안  참조

error: 
dp문제로 풀려했지만 다른 방향에서 온 길임에도 이미 왔던 dfs가 dp의 값을 매겨
그것보다 더 큰 값일 경우 진행하지 못하게 해 실패가 발생.
이 때, dp의 설정을 온 방향까지 추가해 넣어야 함.
"""
from collections import deque

def solution(board):
    result = 10000
    N = len(board)
    direction = [[0, 1, 0], [1, 0, 1], [0, -1, 2], [-1, 0, 3]]
    dp = [[[10000] * N for i in range(N)] for j in range(4)]
    queue = deque()
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    while queue:
        x, y, m, d = queue.popleft()
        for i in range(4):
            new_x = x + direction[i][0]
            new_y = y + direction[i][1]
            if -1 < new_x < N and -1 < new_y < N and board[new_x][new_y] == 0:
                new_m = m + 1
                if not d == direction[i][2]:
                    new_m += 5
                if new_m < dp[direction[i][2]][new_x][new_y]:
                    dp[direction[i][2]][new_x][new_y] = new_m
                    if new_x == N-1 and new_y == N-1:
                        continue
                    queue.append([new_x, new_y, new_m, direction[i][2]])
    for i in range(4):
        result = min([result, dp[i][N-1][N-1]])
    return result * 100