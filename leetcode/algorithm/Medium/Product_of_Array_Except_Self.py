class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        
        prefix = 1
        for i in range(len(nums)):
            answer[i]=prefix 
            prefix *=  nums[i]
        ##먼저 곱하고 prefix를 조정하므로 현재값을 뺀 이전값까지만 곱해짐
            
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i]*=suffix
            suffix *= nums[i]
        return answer
        ##역순으로 곱하면서 이후값들을 곱함
        ##=> 따라서 현재값을 뺀 앞과 뒤의 값들을 모두 곱하게 됨