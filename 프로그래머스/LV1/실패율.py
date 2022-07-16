def solution(N, stages):
    answer = []
    failure_rate=dict()
    for i in range(1,N+1):
        failed,total=0,0
        for person in stages:
            if person<i:
                continue
            elif person==i:
                failed+=1
            total+=1
        failure_rate[i]=failed/total if total!=0 else 0
    answer = list(map(lambda x:x[0], sorted(failure_rate.items(), key=lambda x:x[1], reverse=True)))
    return answer