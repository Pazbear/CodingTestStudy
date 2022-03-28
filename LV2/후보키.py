from itertools import combinations
def solution(relation):
    prev_arr = [i for i in range(len(relation[0]))]
    candidate_key = []
    for i in range(len(relation[0])):
        for cb in list(combinations(prev_arr, i+1)):
            temp_arr = []
            for j in range(len(relation)):
                temp_arr.append('_'.join([relation[j][cb_i] for cb_i in cb]))
            if len(temp_arr) == len(set(temp_arr)):
                if checkMinimality(candidate_key, list(cb)):
                    candidate_key.append(list(cb))
    return len(candidate_key)

def checkMinimality(candidate_key, arr):
    for key in candidate_key:
        if len(arr) == len(set(arr+key)):
            return False
    return True