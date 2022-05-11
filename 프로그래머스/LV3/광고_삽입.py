"""
브루트포스로 풀었지만 실패 => dp로 풀어야함
답안 참조
"""
"""
오답

def solution(play_time, adv_time, logs):
    answer = ''
    adv_h, adv_m, adv_s = map(int, adv_time.split(":"))
    
    s_time, e_time = [], []
    for log in logs:
        s_log, e_log = log.split("-")
        s_time.append(list(map(int, s_log.split(':'))))
        e_time.append(list(map(int, e_log.split(':'))))
    s_temp, e_temp = [0,0,0], [adv_h, adv_m, adv_s]
    total_time = 0
    answer = [0,0,0]
    for i in range(len(s_time)):
        t = min(toSec(e_time[i]), toSec(e_temp)) - max(toSec(s_time[i]), toSec(s_temp))
        total_time += t if t > 0 else 0
    for i in range(len(s_time)):
        s_temp, e_temp = s_time[i], [s_time[i][0]+adv_h,s_time[i][1]+adv_m,s_time[i][2]+adv_s]
        temp_total_time=0
        for j in range(len(s_time)):
            t = min(toSec(e_time[j]), toSec(e_temp)) - max(toSec(s_time[j]), toSec(s_temp))
            temp_total_time += t if t > 0 else 0
        if temp_total_time > total_time:
            answer = s_time[i]
    return ':'.join(map(toDateStr,answer))

def toSec(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def toDateStr(time):
    return '0'+str(time) if len(str(time))==1 else str(time)

"""
"""
정답
"""
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3 구간별 시청자수 기록
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4 모든 구간 시청자 누적 기록
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5 가장 시청자수가 많은 구간 탐색
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time] #끝난 구간의 시청자수 - 시작한 구간의 시청자수
                max_time = i - adv_time + 1
        else: #반복문 시작 때
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s
