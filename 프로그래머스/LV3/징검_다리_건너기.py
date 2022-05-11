"""
이분탐색
"""
def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

"""
정확도만 통과
def solution(stones, k):
    answer=0
    while True:
        isZero = 0
        i=0
        while i<len(stones):
            if stones[i]==0:
                zeroCnt=0
                for j in range(i, len(stones)):
                    if stones[j]==0:
                        zeroCnt+=1
                        if zeroCnt>=k:
                            return answer
                    else:
                        i=j
                        stones[i]-=1
                        break
            else:
                stones[i]-=1
            i+=1
            if i==len(stones):
                answer+=1
        
        
    return answer
"""