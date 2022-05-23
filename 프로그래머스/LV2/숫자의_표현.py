def solution(n):
    start=1
    result = 0
    sum=0
    for i in range(1,n+1):
        sum+=i
        if sum==n:
            result+=1
        elif sum > n:
            while sum > n:
                sum-=start
                start+=1
            if sum==n:
                result+=1
        
    return result