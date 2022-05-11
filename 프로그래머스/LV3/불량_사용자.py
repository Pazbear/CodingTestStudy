from collections import defaultdict
def solution(user_id, banned_id):
    answer = 0
    #제제된 id set들
    banned_id_set = []
    #dfs에서 사용할 이미 제제된 id 목록
    banned = [False for _ in user_id]
    dfs(user_id, banned_id, 0, banned_id_set, banned)

    return len(banned_id_set)

def dfs(user_id, banned_id, banned_index, banned_id_set, banned):
    if banned_index == len(banned_id):
        tmp = sorted([user_id[i] for i in range(len(banned)) if banned[i]==True])
        if tmp not in banned_id_set:
            banned_id_set.append(tmp)
        return
    for i in range(len(user_id)):
        if not banned[i]:
            if len(user_id[i])==len(banned_id[banned_index]):
                tof=True
                for j in range(len(user_id[i])):
                    if banned_id[banned_index][j] != '*' and banned_id[banned_index][j]!=user_id[i][j]:
                        tof=False
                        break
                if tof:
                    banned[i]=True
                    dfs(user_id, banned_id, banned_index+1, banned_id_set, banned)
                    banned[i]=False