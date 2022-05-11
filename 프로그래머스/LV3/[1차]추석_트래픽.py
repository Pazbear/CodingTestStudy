def solution(lines):
    answer = 0
    timeLog=[]
    for line in lines:
        _, end_time, process_time = line.split()
        h, m, s, ms = end_time.replace('.',':').split(':')
        total_ms = getTotalms(h,m,s,ms)
        process_time = int(float(process_time[:len(process_time)-1])*1000)
        timeLog.append([total_ms - process_time+1,total_ms])


    for i in range(len(timeLog)):
        time = timeLog[i][1]
        cnt = 0
        for j in range(i,len(timeLog)):
            if time>timeLog[j][0]-1000: ## 끝나는 시간이 이후의 시작시간의 1초 내에 있을 때
                cnt+=1
        answer = max(answer,cnt)

            
    return answer

def getTotalms(h,m,s,ms):
    return int(h)*3600*1000+int(m)*60*1000+int(s)*1000+int(ms)