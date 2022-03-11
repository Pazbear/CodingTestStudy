import math
def solution(fees, records):
    answer={}
    carTimeLog = {}
    for record in records:
        t, car_num, type = record.split()
        if type == "IN":
            carTimeLog[car_num] = t
            if not car_num in answer:
                answer[car_num]=0
        else:
            answer[car_num]+=calculateTime(carTimeLog[car_num], t)
            carTimeLog[car_num]=-1
    for car_num in carTimeLog:
        if carTimeLog[car_num] !=-1:
            answer[car_num]+=calculateTime(carTimeLog[car_num], "23:59")
    return [calculateFee(answer[a], fees) for a in sorted(answer)]

#두 시각을 받아 시간 계산
def calculateTime(in_time, out_time):
    in_h, in_m = in_time.split(':')
    out_h, out_m = out_time.split(':')
    in_ms = int(in_h)*60+int(in_m)
    out_ms = int(out_h)*60+int(out_m)
    return out_ms - in_ms

#시간에 따른 요금 계산
def calculateFee(time, fees):
    if fees[0]>= time:
        return fees[1]
    else:
        return fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]