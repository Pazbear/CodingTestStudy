def solution(key, lock):
    answer = True
    len_N = len(lock)
    len_M = len(key)
    extended_lock = [[0 for _ in range(len_N*3)] for _ in range(len_N*3)]
    for i in range(len_N):
        for j in range(len_N):
            extended_lock[len_N+i][len_N+j]=lock[i][j]
    for i in range(4):
        key = turnKeyTo90ClockDir(key)
        for j in range(len_N-(len_M-1), len_N * 2):
            for k in range(len_N-(len_M-1), len_N * 2):
                if isRightKey(key, extended_lock, j, k):
                    return True
    return False

def isRightKey(key, lock, keyj, keyk):
    temp = [[lock[i][j] for j in range(len(lock[i]))] for i in range(len(lock))]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[i+keyj][j+keyk] = key[i][j] + temp[i+keyj][j+keyk]
    len_lock = len(lock)//3
    for i in range(len_lock, len_lock*2):
        for j in range(len_lock, len_lock*2):
            if temp[i][j]==2 or temp[i][j]==0:
                return False
    return True

def turnKeyTo90ClockDir(key):
    len_m = len(key)
    temp = [[0 for _ in range(len_m)] for _ in range(len_m)]
    for i in range(len_m):
        for j in range(len_m):
            temp[j][len_m-i-1] = key[i][j]
    return temp