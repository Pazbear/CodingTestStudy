from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist)+1
    len_weak = len(weak)
    for i in range(len(weak)): #확장배열 (두배로 늘림)
        weak.append(weak[i]+n)
    dist_perm = list(map(list, permutations(dist, len(dist)))) #모든 경우의 수
    
    for i in range(len_weak):
        start = [weak[j] for j in range(i, i+len_weak)]
        for j in range(len(dist_perm)):
            result = 1
            dist_distance = 0
            check_len = start[0]+dist_perm[j][dist_distance]
            for k in range(len_weak):
                if start[k]>check_len: #확인가능거리가 최대 거리를 넘지 못했을경우
                    result += 1
                    if result > len(dist):
                        break
                    dist_distance +=1
                    check_len = start[k] + dist_perm[j][dist_distance]
            
            answer = min(answer, result)
    
    if answer > len(dist):
            return -1
    
    return answer