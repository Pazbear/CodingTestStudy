def solution(n):
    arr = [0 for _ in range(n+1)]
    arr[0]=0
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=(arr[i-1]+arr[i-2])%1234567
    return arr[n]