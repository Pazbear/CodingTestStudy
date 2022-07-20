def solution(n):
    prime_nums = [0]*(n+1)
    prime_nums[1]=1
    for i in range(2, (n+1)//2+1):
        if prime_nums[i]==1:
            continue
        for j in range(2*i, n+1, i):
            if prime_nums[j]==0:
                prime_nums[j]=1
    answer=0
    for i in range(1, n+1):
        answer+= 1 if prime_nums[i]==0 else 0
    return answer