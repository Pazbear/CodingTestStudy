class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total =0
        for num in nums:
            total+=num
        dp=[[0 for _ in range(total*2+1)] for _ in range(len(nums))]
        dp[0][nums[0]+total]=1
        dp[0][-nums[0]+total]+=1
        for i in range(1,len(nums)):
            for sum in range(-total, total+1):
                if dp[i-1][sum+total]>0:
                    dp[i][sum+nums[i]+total] += dp[i-1][sum+total]
                    dp[i][sum-nums[i]+total] += dp[i-1][sum+total]
                    
        return 0 if target > total else dp[len(nums)-1][target+total]