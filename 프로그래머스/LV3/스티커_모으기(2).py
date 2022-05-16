def solution(sticker):
    answer = 0
    if len(sticker)==1:
        return sticker[0]
    elif len(sticker)==2:
        return max(sticker[0], sticker[1])
    elif len(sticker)==3:
        return max(sticker[0], max(sticker[1],sticker[2]))
    #맨 앞과 맨뒤를 동시에 사용하지 못하므로 맨앞을 자른 배열과 맨뒤를 자른 배열 두 개로 나눔
    temp1= sticker[1:]
    temp2= sticker[:-1]
    
    return max(findmax(temp1), findmax(temp2))

def findmax(arr):
    dp=[0 for _ in arr]
    for i in range(len(arr)):
        if i == 0:
            dp[i]=arr[i]
        elif i==1:
            dp[i]=arr[i]
        elif i==2:
            dp[i]=dp[0]+arr[i]
        else:
            dp[i]=max(dp[i-2], dp[i-3])+arr[i]
    return max(dp[-1], dp[-2])