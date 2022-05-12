import math
def solution(n, stations, w):
    answer = 0
    covered = 0
    len_covered = 2*w+1
    for station in stations:
        s_covered, e_covered = station-w, station+w
        if s_covered > covered:
            answer+=math.ceil((s_covered - covered-1)/len_covered)
        covered = e_covered
    if n > covered:
        answer+=math.ceil((n-covered)/len_covered)
    return answer