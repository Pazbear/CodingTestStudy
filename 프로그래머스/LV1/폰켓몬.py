def solution(nums):
    select_n = len(nums)//2
    nums = set(nums)
    return min(len(nums), select_n)