from itertools import combinations
def solution(nums):
    answer = 0
    prime_nums = [0]*3000
    for i in range(2, 3000//2+1):
        if prime_nums[i]==1:
            continue
        for j in range(2*i, 3000, i):
            if prime_nums[j]==0:
                prime_nums[j]=1
    for combi_nums in list(combinations(nums, 3)):
        if prime_nums[sum(combi_nums)] == 0:
            answer+=1
    return answer
