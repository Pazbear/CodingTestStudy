def solution(num):
    cnt=0
    while cnt < 500 and num !=1:
        num = num*3 +1 if num%2 else num//2
        cnt+=1
    return -1 if cnt==500 else cnt